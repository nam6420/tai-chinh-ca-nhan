from __future__ import annotations
import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'learning' / 'practice' / 'models'))
import market_returns as m


class MarketReturns(unittest.TestCase):
    def test_pv_fv_inverse_including_negative_rate(self):
        for amount, rate, periods in [(150, .08, 3), (25, .06, 4), (100, -.02, 5), (0, .1, 0)]:
            self.assertAlmostEqual(m.present_value(m.future_value(amount, rate, periods), rate, periods), amount)

    def test_rate_conversion_does_not_divide_effective_rate(self):
        monthly = m.equivalent_period_rate(.12, 12)
        self.assertAlmostEqual((1 + monthly) ** 12 - 1, .12)
        self.assertNotAlmostEqual(monthly, .12 / 12)
        self.assertAlmostEqual(m.effective_annual_rate(.12, 12), .12682503013196977)

    def test_contribution_timing_and_zero_rate(self):
        self.assertEqual(m.monthly_contributions(10, 2, 0, 36), 82)
        end = m.monthly_contributions(0, 2, .005, 36)
        start = m.monthly_contributions(0, 2, .005, 36, 'start')
        self.assertAlmostEqual(start, end * 1.005)
        # Lặp từng tháng phải khớp công thức niên kim cuối kỳ.
        self.assertAlmostEqual(end, 2 * ((1.005 ** 36 - 1) / .005))
        self.assertAlmostEqual(m.monthly_contributions(10, 2, .005, 36), 90.6390151776)

    def test_portfolio_accounting_and_rebalance_conserves_value(self):
        amounts, rates = [50, 30, 20], [.1, -.05, .02]
        r = m.evolve(amounts, rates)
        self.assertAlmostEqual(r['total'], 103.9)
        self.assertAlmostEqual(m.weighted_return([.5, .3, .2], rates), r['total'] / 100 - 1)
        self.assertAlmostEqual(sum(r['weights']), 1)
        reset = m.rebalance(r['amounts'], [.5, .3, .2])
        self.assertAlmostEqual(sum(reset['transfers']), 0)
        self.assertAlmostEqual(sum(reset['targets']), r['total'])
        self.assertAlmostEqual(m.evolve(r['amounts'], [-.2, .1, 0])['total'], 95.75)
        self.assertAlmostEqual(m.evolve(reset['targets'], [-.2, .1, 0])['total'], 96.627)

    def test_static_book_depth_and_limit(self):
        asks = [(20100, 300), (20300, 100)]
        r = m.book_fill(asks, 400)
        self.assertEqual(r['cost'], 8060000)
        self.assertEqual(r['average_price'], 20150)
        limited = m.book_fill(asks, 400, 20100)
        self.assertEqual((limited['filled'], limited['unfilled']), (300, 100))
        empty = m.book_fill(asks, 400, 20000)
        self.assertIsNone(empty['average_price'])

    def test_issuance_and_valuation_units(self):
        self.assertEqual(m.issuance(200000, 10000, 100e6), 1.9e9)
        self.assertEqual(m.market_cap(12500, 80e6), 1e12)
        self.assertEqual(m.enterprise_value(1e12, 400e9, 150e9), 1.25e12)
        self.assertEqual(m.market_cap(250, 14776353000), 3694088250000)
        self.assertAlmostEqual(m.ownership(10000, 1100000), 1 / 110)

    def test_return_conventions(self):
        self.assertAlmostEqual(m.total_return(50, 52, 3), .1)
        self.assertAlmostEqual(m.compound_returns([.1, -.1]), -.01)
        self.assertEqual(m.compound_returns([-.1, -1, .2]), -1)
        self.assertAlmostEqual(m.real_return(.08, .04), .0384615384615385)
        self.assertAlmostEqual(m.currency_return(.09, -.05), .0355)
        self.assertAlmostEqual((1 + m.cagr(100, 234, 5)) ** 5, 2.34)
        self.assertAlmostEqual(m.after_fee_growth(100, .05, .01, 2), 108.056025)

    def test_rejects_missing_or_inconsistent_inputs(self):
        calls = [lambda: m.future_value(100, -1, 3), lambda: m.cagr(0, 100, 5),
                 lambda: m.market_cap(math.nan, 1), lambda: m.market_cap(100, None),
                 lambda: m.monthly_contributions(10, 2, .01, 1.5),
                 lambda: m.weighted_return([.5, .4], [.1, .1]),
                 lambda: m.weighted_return([.5, .5], [.1]),
                 lambda: m.rebalance([10], [.5, .5]),
                 lambda: m.real_return(.1, -1)]
        for call in calls:
            with self.assertRaises(ValueError):
                call()
