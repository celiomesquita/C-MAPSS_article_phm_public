import unittest
import numpy as np
import pandas as pd
import analyse_explainability_13b as a


class ExplanationAnalysisTests(unittest.TestCase):
    def test_identical_constant_rank_is_not_identified(self):
        r=a.rank_comparison(np.zeros(21),np.zeros(21))
        self.assertFalse(r['identified'])
        self.assertTrue(np.isnan(r['spearman']))
        self.assertTrue(r['boundary_tie_a'])

    def test_opposite_sensor_ranks_are_discordant(self):
        r=a.rank_comparison(np.arange(21.),-np.arange(21.))
        self.assertAlmostEqual(r['spearman'],-1)
        self.assertEqual(r['shared_top5'],0)

    def test_missing_dates_are_not_zero_sensitivity(self):
        f=pd.DataFrame(dict(subset='FD001',repeat=1,fold=1,unit=1,policy_id='x',method='ISO',delay=1,
                            phase='global',kind='channel',epsilon=1.,variant=[1,2],decision=[np.nan,10.],
                            base_decision=np.nan,delta_removal=np.nan,within_support=False,
                            reached=[True,False],base_reached=True))
        r=a.engine_actions(f).iloc[0]
        self.assertEqual(r.paired_dates,0)
        self.assertTrue(np.isnan(r.mean_abs_delta))
        self.assertEqual(r.presence_flip,.5)

    def test_paired_bootstrap_retains_missing_engine_denominator(self):
        f=pd.DataFrame(dict(subset='FD001',repeat=1,phase='global',kind='channel',epsilon=1.,
                            policy_id='a',reference='b',unit=np.arange(1,101),value=np.r_[np.nan,np.arange(99.)],
                            presence_difference=0.))
        indices={'FD001_r1':np.random.default_rng(1).integers(0,100,(2000,100))}
        r=a.boot_contrasts(f,indices).iloc[0]
        self.assertEqual(r.value_engines,99)
        self.assertEqual(r.presence_difference_engines,100)
        self.assertAlmostEqual(r.value,49)
        self.assertLess(r.value_lo,r.value_hi)


if __name__=='__main__':unittest.main()
