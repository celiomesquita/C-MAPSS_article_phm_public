import unittest
import numpy as np
import pandas as pd
import pilot_loss_decomposition_11b as p


class DecompositionTests(unittest.TestCase):
    def row(self, **kw):
        return dict(endpoint=100, delay=2, decision=60., method='ISO') | kw

    def test_crossing_memory_and_warmup(self):
        g = pd.DataFrame(dict(cycle=[20,21,39,40], hi=[.4,.8,.9,.9]))
        self.assertEqual(p.information(g,100), (20.,39.))

    def test_unobserved_access_and_endpoint_not_used(self):
        g = pd.DataFrame(dict(cycle=[20,100], hi=[1.,.4]))
        self.assertTrue(np.isnan(p.information(g,100)[0]))
        g = pd.DataFrame(dict(cycle=[20], hi=[.4]))
        self.assertTrue(np.isnan(p.information(g,30)[1]))

    def test_oracles_early_late_missing(self):
        self.assertEqual(p.oracle(100,97,40),97)
        self.assertEqual(p.oracle(100,97,99),99)
        self.assertTrue(np.isnan(p.oracle(100,97,np.nan)))
        self.assertTrue(np.isnan(p.oracle(100,97,100)))

    def test_deadline_equality_is_not_late_planning(self):
        a=p.outcomes(97,100,2,97)
        b=p.outcomes(98,100,2,97)
        self.assertEqual((a['J'],a['B'],a['reached']),(0,0,0))
        self.assertEqual((b['J'],b['B'],b['exact']),(1,1,1))

    def test_strict_late_and_missing_stay_different(self):
        a=p.outcomes(99,100,2,97)
        b=p.outcomes(np.nan,100,2,97)
        self.assertEqual((a['late'],a['missing']),(1,0))
        self.assertEqual((b['late'],b['missing'],b['B']),(0,1,3))
        self.assertTrue(np.isnan(b['decision']))

    def test_warmup_and_post_parts_are_additive(self):
        r=p.decompose(self.row(decision=90),20,39,70)
        for k in ['J','B','W']:
            self.assertEqual(r[k+'_total'],r[k+'_det']+r[k+'_post'])
            self.assertEqual(r[k+'_det'],r[k+'_crossing']+r[k+'_warmup'])
        self.assertEqual(r['B_warmup'],11)

    def test_early_policy_can_waste_life_without_planning_loss(self):
        r=p.decompose(self.row(),40,40,1)
        self.assertEqual((r['J_total'],r['J_det'],r['W_post']),(0,0,37))

    def test_non_nested_and_age_are_contextual(self):
        self.assertFalse(p.decompose(self.row(decision=30),40,40,1)['information_matched'])
        self.assertFalse(p.decompose(self.row(method='AGE'),40,40,1)['information_matched'])

    def test_late_oracle_cost_component_may_be_negative(self):
        r=p.decompose(self.row(decision=np.nan),99,99,1)
        self.assertLess(1/r['A_N']-1/r['O_N'],0)
        self.assertEqual(r['A_reached'],1)

    def test_zero_loss_share_is_undefined_and_bootstrap_is_paired(self):
        rows=[]
        for unit in range(1,101):
            row=self.row(decision=50,unit=unit,subset='FD001',repeat=1,policy_id='ISO_D2')
            rows.append(row | p.decompose(row,40,40,1))
        ix=np.random.default_rng(1).integers(0,100,(2000,100))
        out=p.summaries(pd.DataFrame(rows),{'FD001_r1':ix})
        self.assertTrue(out.J_det_share.isna().all())
        self.assertTrue(out.J_share_undefined_bootstrap.eq(2000).all())
        np.testing.assert_allclose(out.cost_total,out.cost_det+out.cost_post)


if __name__ == '__main__':
    unittest.main()
