import unittest
import joblib
import numpy as np
import pandas as pd
import explainability_core_13b as c
import pilot_f_uncertainty_10 as p10


class ExplanationTests(unittest.TestCase):
    def model(self):
        return dict(stats=dict(channels=['s1','s3'],direction=np.array([1.,-1.]),scale=np.array([2.,3.])),beta=np.array([.4,.6]))

    def raw(self):
        return np.random.default_rng(17).normal(size=(80,21)).cumsum(axis=0)

    def test_signed_sum_clipping_cancellation(self):
        x=np.array([[2.,-1.5],[2.,1.],[-2.,1.],[0.,0.]])
        h,a,s=c.bounded_contributions(x)
        np.testing.assert_allclose(h,[.5,0.,1.,1.])
        np.testing.assert_allclose(a.sum(axis=1),1-h)
        self.assertLess(a[0,1],0)

    def test_raw_perturbation_equals_linear_preprocessing(self):
        raw=self.raw();cycles=np.arange(1,81);shifts=np.ones((2,21));shifts[0]=0
        for cutoff in [None,60]:
            C,channels,w=c.base_contributions(raw,self.model())
            H,_=c.health_paths(C,channels,w,shifts,cycles,cutoff)
            changed=raw+c.ramp(cycles,cutoff)[:,None]
            cc,_,_=c.base_contributions(changed,self.model())
            direct=c.bounded_contributions(cc[19:])[0]
            np.testing.assert_allclose(H[1],direct,atol=1e-12)

    def test_reference_and_prefix_causality(self):
        raw=self.raw();C,ch,w=c.base_contributions(raw,self.model())
        H,S=c.health_paths(C,ch,w,np.ones((1,21)),np.arange(1,81))
        short,_,_=c.base_contributions(raw[:55],self.model())
        h,s=c.health_paths(short,ch,w,np.ones((1,21)),np.arange(1,56))
        self.assertEqual(H[0,0],1)
        np.testing.assert_allclose(H[:,:36],h)
        np.testing.assert_allclose(S[:,:36],s,equal_nan=True)

    def test_noise_uses_only_fit_units_and_keeps_constant_channels(self):
        frames=[]
        for unit in range(1,4):
            x=self.raw()[:25]+unit
            x[:,20]=1
            frame=pd.DataFrame(x,columns=c.SENSORS).assign(unit=unit,cycle=np.arange(1,26))
            frames.append(frame)
        data=pd.concat(frames,ignore_index=True)
        noise=c.noise_model(data)
        self.assertEqual(noise['fit_units'],[1,2,3])
        self.assertNotIn(20,noise['active'])
        data.loc[data.cycle.gt(20),'s1']=999999
        np.testing.assert_allclose(c.noise_model(data)['cov'],noise['cov'])
        v,shifts=c.variants(noise)
        self.assertEqual((v.epsilon.eq(0)).sum(),1)
        np.testing.assert_allclose(shifts[:,20],0)

    def rows(self,method='HI_MARKER',value=0):
        return pd.DataFrame([dict(method=method,selected_value=value,delay=2,reserve=15,q_late=0,
                                  control_age=60,endpoint=80,policy_id='test')])

    def test_event_memory_wait_and_endpoint_stop(self):
        t=np.arange(20,80);H=np.ones((1,len(t)));H[0,0]=.4
        f=np.ones_like(H)*100
        self.assertEqual(c.actions(self.rows(),t,H,f,f)[0]['decision'][0],39)
        self.assertEqual(c.actions(self.rows('HI_WAIT_SELECTED',5),t,H,f,f)[0]['decision'][0],44)
        self.assertTrue(np.isnan(c.actions(self.rows('HI_WAIT_SELECTED',50),t,H,f,f)[0]['decision'][0]))

    def test_age_invariance_and_missing_stays_missing(self):
        t=np.arange(20,80);H=np.ones((2,len(t)));f=H*999
        np.testing.assert_allclose(c.actions(self.rows('AGE'),t,H,f,f)[0]['scheduled'],60)
        self.assertTrue(c.actions(self.rows(),t,H,f,f)[0]['missing'].all())

    def test_public_predict_matches_explicit_ensemble_and_local_prefix(self):
        bundle=joblib.load(p10.OUT/'models_FD001_r1_f1.joblib')
        H=np.linspace(.9,.2,61)[None,:];S=np.full_like(H,np.nan);S[:,19:]=-.01
        ISO,RF=c.forecasts(bundle,H,S)
        np.testing.assert_allclose(ISO[0,19:],bundle['predictors']['ISO']['model'].predict(H[0,19:]),atol=1e-9)
        np.testing.assert_allclose(RF[0,19:],bundle['predictors']['RF_SLOPE']['model'].predict(np.c_[H[0,19:],S[0,19:]]),atol=1e-9)
        _,reuse=c.forecasts(bundle,H,S,RF[0],65)
        np.testing.assert_allclose(RF,reuse,equal_nan=True)

    def test_support_baseline_and_no_future_shift(self):
        data=pd.concat([pd.DataFrame(self.raw(),columns=c.SENSORS).assign(unit=i,cycle=np.arange(1,81)) for i in [1,2]])
        noise=c.noise_model(data)
        raw=self.raw();outside=c.support(raw,np.arange(1,81),np.zeros((2,21)),noise)
        np.testing.assert_array_equal(outside[0],outside[1])
        np.testing.assert_allclose(c.ramp(np.arange(1,81),60)[:20],0)

    def test_policy_support_records_use_observed_prefix_and_all_variants(self):
        import pilot_explainability_13b as p
        group=self.rows('AGE').assign(decision=58.,scheduled=60.,has_decision=True,
                                      reached_endpoint=False,selection_feasible=np.nan)
        noise=c.noise_model(pd.concat([pd.DataFrame(self.raw(),columns=c.SENSORS).assign(unit=i,cycle=np.arange(1,81)) for i in [1,2]]))
        variants,_=c.variants(noise);variants=variants.iloc[:2].copy()
        t=np.arange(20,80);H=np.ones((2,len(t)));F=H*100
        outside=np.zeros((2,78),dtype=bool);outside[1,70]=True
        records=p.policy_records(group,{},H,t,F,F,variants,outside,'global')
        self.assertEqual(len(records),2)
        self.assertTrue(records[1]['within_support'])
        outside[1,40]=True
        records=p.policy_records(group,{},H,t,F,F,variants,outside,'global')
        self.assertFalse(records[1]['within_support'])


if __name__=='__main__':unittest.main()
