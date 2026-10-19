import unittest
import numpy as np
import pandas as pd
import pilot_hi_influence_13c as p


class InfluenceTests(unittest.TestCase):
    def test_effective_weights_align_channels(self):
        health=dict(stats=dict(channels=['s3','s1'],direction=np.array([-1,1]),scale=np.array([2,4])),beta=np.array([6,8]))
        expected=np.zeros(21);expected[2]=-3;expected[0]=2
        np.testing.assert_allclose(p.effective_weights(health),expected)

    def test_missing_crossing_preserved(self):
        frame=pd.DataFrame(dict(unit=[1,1,2,2],cycle=[20,21,20,21],hi=[1,.5,1,.6]))
        m=p.markers(frame)
        self.assertEqual(m.loc[1],21);self.assertTrue(np.isnan(m.loc[2]))

    def test_rank_deficient_design(self):
        c,s=p.condition(np.array([[1.,1.],[2.,2.],[3.,3.]]))
        self.assertTrue(np.isinf(c));self.assertEqual(len(s),2)

    def test_ridge_improves_condition(self):
        x=np.array([[1.,1.],[2.,2.]])
        c,_=p.condition(np.vstack([x,np.sqrt(.1)*np.eye(2)]))
        self.assertTrue(np.isfinite(c))

    def test_refit_requires_24_engines(self):
        with self.assertRaises(AssertionError):
            p.refit(pd.DataFrame({'unit':[1,2]}),{},'FD001','full')


if __name__=='__main__': unittest.main()
