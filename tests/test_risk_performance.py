import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'learning/practice/models'))
import risk_performance as m


class RiskPerformance(unittest.TestCase):
    def test_path_volatility_and_end_wealth(self):
        values = [100, 110, 88, 101.2, 106.26]
        rates = m.returns(values)
        for actual, expected in zip(rates, [.1, -.2, .15, .05]):
            self.assertAlmostEqual(actual, expected)
        self.assertAlmostEqual(m.sample_volatility(rates) ** 2, .0725 / 3)
        for actual, expected in zip(m.drawdowns(values), [0, 0, -.2, -.08, -.034]):
            self.assertAlmostEqual(actual, expected)
        self.assertAlmostEqual(m.recovery(.2), .25)
        self.assertAlmostEqual(m.recovery(.5), 1)
        self.assertAlmostEqual(m.twr(values[:-1], values[1:]), .0626)

    def test_real_rounded_sp_inputs(self):
        # Berkshire thư2024 PDF trang15: S&P có cổ tức, 2008/2009.
        self.assertAlmostEqual(100 * (1 - .37) * (1 + .265), 79.695)
        self.assertAlmostEqual(m.recovery(.37), 100 / 63 - 1)
        # 2022/2023 theo đúng cùng bảng làm tròn.
        self.assertAlmostEqual((1 - .181) * (1 + .263) - 1, .034397)

    def test_book_does_not_invent_liquidity(self):
        result = m.sell_book([(20000, 200), (19800, 300), (19000, 500)], 1200)
        self.assertEqual(result['filled'], 1000)
        self.assertEqual(result['unfilled'], 200)
        self.assertEqual(result['proceeds'], 19440000)
        self.assertEqual(result['average'], 19440)
        self.assertIsNone(m.sell_book([], 10)['average'])

    def test_cashflows_twr_and_irr_residual(self):
        self.assertAlmostEqual(m.twr([100, 210, 150], [110, 189, 180]), .188)
        flows = [-100, -100, 39, 180]
        rate = m.bracketed_irr(flows, [0, 1, 2, 3])
        self.assertAlmostEqual(rate, .0398248913175)
        self.assertAlmostEqual(m.npv(rate, flows, [0, 1, 2, 3]), 0)
        self.assertAlmostEqual(m.npv(rate, [x * 1000 for x in flows], [0, 1, 2, 3]), 0, places=7)
        self.assertAlmostEqual(m.twr([100, 110, 99], [110, 99, 118.8]), .188)

    def test_xirr_actual_days_and_365_convention(self):
        flows = [-100, -100, 39, 180]
        dates = ['2023-01-01', '2023-07-01', '2024-07-01', '2025-01-01']
        rate = m.xirr(flows, dates)
        self.assertAlmostEqual(rate, .05599660543654)
        self.assertAlmostEqual(m.npv(rate, flows, [0, 181 / 365, 547 / 365, 731 / 365]), 0)

    def test_body_and_answers_extra_cases(self):
        self.assertAlmostEqual(110 / 106.26 - 1, .0351966873706)
        self.assertAlmostEqual(1.188 ** (365 / 731) - 1, .0898257029428)
        self.assertAlmostEqual(m.bracketed_irr([-100, -100, 229.7397], [0, 1, 2]), .0960567032534)

    def test_multiple_roots_not_a_unique_answer(self):
        flows, times = [-100, 230, -132], [0, 1, 2]
        for rate in [.1, .2]:
            self.assertAlmostEqual(m.npv(rate, flows, times), 0)
        self.assertAlmostEqual(m.bracketed_irr(flows, times, .05, .15), .1)
        self.assertAlmostEqual(m.bracketed_irr(flows, times, .15, .25), .2)

    def test_missing_inputs_rejected(self):
        calls = [lambda: m.returns([100]), lambda: m.returns([100, None]),
                 lambda: m.drawdowns([100, float('nan')]), lambda: m.recovery(1),
                 lambda: m.sample_volatility([.1]), lambda: m.twr([100], [110, 120]),
                 lambda: m.bracketed_irr([-100, -20], [0, 1]),
                 lambda: m.xirr([-100, 110], ['2024-01-01', '2023-01-01'])]
        for call in calls:
            with self.assertRaises(ValueError):
                call()
