import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'learning/practice/models'))
import evidence_lab as m


class EvidenceLab(unittest.TestCase):
    def test_selection_does_not_use_holdout(self):
        selected = max(m.RULES, key=lambda k: m.compound(m.RULES[k][:4]))
        self.assertEqual(selected, 'A')
        self.assertAlmostEqual(m.compound(m.RULES[selected][:4]), .16985856)
        self.assertAlmostEqual(m.compound(m.RULES[selected][4:]), -.0591)
        self.assertAlmostEqual(m.compound([m.net_period(x, 2, .005) for x in m.RULES['A'][4:]]), -.0784)
        self.assertAlmostEqual(m.compound([m.net_period(x, 2, .005) for x in m.RULES['B'][4:]]), 0)

    def test_cost_on_sum_of_both_legs(self):
        self.assertAlmostEqual(m.net_period(.005, .8, .0015), .0038)
        self.assertAlmostEqual(100e6 * m.net_period(.005, .8, .0015), 380000)
        self.assertAlmostEqual(m.net_period(.01, 2, .005), 0)

    def test_publication_date_and_restatement(self):
        self.assertFalse(m.available('2021-12-31', '2022-02-15', '2022-01-03'))
        self.assertTrue(m.available('2021-12-31', '2022-02-15', '2022-02-16'))
        self.assertFalse(m.available('2021-12-31', '2023-03-01', '2022-02-16'))

    def test_survivors_change_population_not_missing_zero(self):
        all_returns = [.1, .05, -.9]
        self.assertAlmostEqual(sum(all_returns) / 3, -.25)
        self.assertAlmostEqual(sum(all_returns[:2]) / 2, .075)
        self.assertNotEqual(sum(all_returns) / 3, sum(all_returns[:2]) / 2)

    def test_independent_trials_probability_not_expectation(self):
        expectation, probability = m.false_positives(100, .05)
        self.assertEqual(expectation, 5)
        self.assertAlmostEqual(probability, .994079470779666)
        self.assertEqual(m.false_positives(1, .05)[0], .05)

    def test_reject_incomplete_or_invalid(self):
        for call in [lambda: m.compound([]), lambda: m.compound([float('nan')]),
                     lambda: m.net_period(.1, -1, .005), lambda: m.false_positives(0, .05)]:
            with self.assertRaises(ValueError):
                call()
