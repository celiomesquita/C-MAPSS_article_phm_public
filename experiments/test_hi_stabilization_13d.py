import unittest
import numpy as np
import pandas as pd
import hi_stabilization_core_13d as core
import pilot_f_uncertainty_10 as p10
from pilot_policy_selection_13a import inner_partitions


class StabilizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.banks={};cls.inputs={}
        for subset in ['FD001','FD003']:
            ids=p10.partitions(p10.SEEDS[0])[0]['fit']
            data=p10.read_inputs('train',subset).loc[lambda x:x.unit.isin(ids)].reset_index(drop=True)
            cls.inputs[subset]=data;cls.banks[subset]=core.engine_bank(data,subset)

    def test_moments_reproduce_original_fits_both_domains(self):
        for subset in self.banks:
            bank=self.banks[subset];ids=sorted(bank);m=core.moments(bank,ids)
            new=core.solve(m,subset,'M18');old=p10.fit_health(self.inputs[subset],subset)
            expected=np.zeros(21)
            for sensor,b,d,s in zip(old['stats']['channels'],old['beta'],old['stats']['direction'],old['stats']['scale']):
                expected[core.SENSORS.index(sensor)]=b*d/s
            np.testing.assert_allclose(new['effective'],expected,atol=1e-8,rtol=1e-7)

    def test_signed_matches_full_row_ridge(self):
        bank=self.banks['FD003'];m=core.moments(bank,sorted(bank));model=core.solve(m,'FD003','SIGNED_01')
        x=np.concatenate([r['x']*model['factors']/np.sqrt(len(bank)*r['n']) for r in bank.values()])
        y=np.concatenate([(1-r['target'])/np.sqrt(len(bank)*r['n']) for r in bank.values()])
        active=model['eligible'];a=np.vstack([x[:,active],np.sqrt(.1)*np.eye(active.sum())]);b=np.r_[y,np.zeros(active.sum())]
        expected=np.linalg.lstsq(a,b,rcond=None)[0]
        np.testing.assert_allclose(model['beta'][active],expected,atol=1e-9)

    def test_engine_weights_not_cycle_weights(self):
        bank=self.banks['FD001'];ids=sorted(bank)[:2];m=core.moments(bank,ids)
        expected=(bank[ids[0]]['gram']+bank[ids[1]]['gram'])/2
        np.testing.assert_allclose(m['gram'],expected)

    def test_inner_partitions_exclude_U_E(self):
        sp=p10.partitions(p10.SEEDS[0])[0]|dict(seed=p10.SEEDS[0])
        parts=inner_partitions(sp)
        self.assertEqual(sorted(sum([p['validation'] for p in parts],[])),sorted(sp['fit']+sp['converter']))
        for part in parts:
            self.assertFalse(set(part['fit'])&set(part['validation']+sp['uncertainty']+sp['evaluation']))

    def test_stability_does_not_override_error_gate(self):
        metrics=pd.DataFrame([dict(candidate=c,engines=40,mse=.1,decisions=40,reached_d1=0,reached_d2=0,
                discordance=0,loo_missing=0,finite_pairs=1000,p95_abs=10.,mean_abs=2.,max_abs=50.) for c in core.CANDIDATES])
        metrics.loc[metrics.candidate=='SIGNED_01',['p95_abs','mse']]=[0.,.106]
        _,chosen=core.choose(metrics)
        self.assertEqual(chosen['selected'],'M18')

    def test_missing_marker_not_imputed(self):
        bank={1:dict(x=np.zeros((5,21)),cycles=np.arange(20,25),end=24,target=np.ones(5))}
        result,_=core.evaluate(bank,1,np.zeros(21))
        self.assertTrue(np.isnan(result['crossing']));self.assertTrue(result['missing']);self.assertTrue(result['reached_d1'])

    def test_duplicate_control_identical(self):
        bank=self.banks['FD001'];m=core.moments(bank,sorted(bank))
        np.testing.assert_array_equal(core.solve(m,'FD001','M18')['effective'],core.solve(m,'FD001','NNLS_01')['effective'])


if __name__=='__main__': unittest.main()
