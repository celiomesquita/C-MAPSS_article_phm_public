import unittest

import numpy as np

import inspection_arm_17b as m
from pilot_extension_16a import engine_expectation


def brute(T, has, D, d, u, entry, W, gamma, pP, pF):
    """Explicit path enumeration over cycles (independent of the vectorised implementation)."""
    tau = m.AGE-d
    times = set(m.inspection_times(T, entry, W).tolist())
    start = min([tau]+list(times))
    out = dict(util=0., late=0., exact=0., missing=0., inspections=0., rejection=0.)

    def walk(t, prob):
        if prob == 0.:
            return
        if has and t > D:
            return
        if (not has) and t > T-1:
            out["util"] += prob*T
            out["missing"] += prob
            return
        loss = u if t >= tau else 0.
        # monitoring invalid -> decision now
        decide(t, prob*loss)
        valid = prob*(1.-loss)
        if has and t == D:
            decide(t, valid)
            return
        if t in times:
            out["inspections"] += valid
            p = m.reject_probability(T, t, W, gamma, pP, pF)
            out["rejection"] += valid*p
            decide(t, valid*p)
            walk(t+1, valid*(1.-p))
        else:
            walk(t+1, valid)

    def decide(t, prob):
        if prob == 0.:
            return
        s = t+d
        out["util"] += prob*min(s, T)
        out["late"] += prob*(s > T)
        out["exact"] += prob*(s == T)

    if has and D < start:
        s = D+d
        return dict(util=min(s, T), late=float(s > T), exact=float(s == T), missing=0., inspections=0., rejection=0.)
    walk(start, 1.)
    return out


class ExpectationTests(unittest.TestCase):
    def cases(self):
        rng = np.random.default_rng(3)
        for _ in range(40):
            T = int(rng.integers(120, 260))
            has = bool(rng.integers(0, 2))
            D = int(rng.integers(100, T+1)) if has else np.nan
            yield T, has, D, int(rng.integers(1, 3)), float(rng.choice(m.US))

    def test_without_rejection_reproduces_p16(self):
        for T, has, D, d, u in self.cases():
            if not has and T-1 < m.AGE-d:
                continue                                      # P16.1 is undefined when the engine ends before the gate
            for entry in ("S2", "S1"):
                h = m.hybrid_expectation(T, has, D, d, u, entry, 60, 1., 0., 0.)
                orig = (D+d) if has else np.nan
                e = engine_expectation(float(T), has, float(D) if has else np.nan, d, float(orig), u)
                if entry == "S2" or h["inspections"] > 0:
                    pass
                if entry == "S2":
                    for k_h, k_e in [("util", "util"), ("late", "late"), ("exact", "exact"), ("missing", "missing")]:
                        self.assertAlmostEqual(h[k_h], e[k_e], places=9)
                    p = m._phm(T, has, D, d, u)
                    self.assertAlmostEqual(p["util"], e["util"], places=9)

    def test_matches_path_enumeration(self):
        for T, has, D, d, u in self.cases():
            for entry, W, g, pP in [("S2", 60, 1., 0.), ("S2", 30, .26, .02), ("S1", 80, 2., 0.), ("S1", 30, 1., .02)]:
                fast = m.hybrid_expectation(T, has, D, d, u, entry, W, g, pP, 1.)
                slow = brute(T, has, D, d, u, entry, W, g, pP, 1.)
                for k in fast:
                    self.assertAlmostEqual(fast[k], slow[k], places=9, msg=(T, has, D, d, u, entry, k))

    def test_certain_rejection_stops_at_first_inspection(self):
        h = m.hybrid_expectation(300, False, np.nan, 2, 0., "S2", 60, 1., 1., 1.)
        self.assertAlmostEqual(h["util"], 129.)
        self.assertAlmostEqual(h["inspections"], 1.)
        h = m.hybrid_expectation(300, False, np.nan, 1, 0., "S1", 60, 1., 1., 1.)
        self.assertAlmostEqual(h["util"], 241.)

    def test_hybrid_never_extends_life_and_never_postpones(self):
        for T, has, D, d, u in self.cases():
            for p in (0., .02):
                h = m.hybrid_expectation(T, has, D, d, u, "S2", 60, 1., p, 1.)
                q = m._phm(T, has, D, d, u)
                self.assertLessEqual(h["util"], q["util"]+1e-9)
                self.assertLessEqual(h["missing"], q["missing"]+1e-9)

    def test_inspections_stop_at_decision_and_exclude_endpoint(self):
        h = m.hybrid_expectation(300, True, 130, 1, 0., "S2", 60, 1., 0., 1.)
        self.assertAlmostEqual(h["inspections"], 1.)          # only t=127 precedes the PHM decision at 130
        h = m.hybrid_expectation(133, False, np.nan, 1, 0., "S2", 60, 1., 0., 0.)
        self.assertAlmostEqual(h["inspections"], 2.)          # 127 and 132; 137 > T-1
        self.assertEqual(m.inspection_times(132, "S2", 60).tolist(), [127, 132][:1])
        self.assertEqual(m.inspection_times(300, "S1", 60).tolist()[0], 240)

    def test_monte_carlo_agrees_with_exact(self):
        rng = np.random.default_rng(11)
        T, D, d, u, W, g, pP = 200, 175, 2, .004, 60, 1., .02
        h = m.hybrid_expectation(T, True, D, d, u, "S2", W, g, pP, 1.)
        times = m.inspection_times(T, "S2", W)
        utils = []
        for _ in range(60000):
            t_dec = None
            for t in range(m.AGE-d, D+1):
                if rng.random() < u:
                    t_dec = t
                    break
                if t == D:
                    t_dec = t
                    break
                if t in times and rng.random() < m.reject_probability(T, t, W, g, pP, 1.):
                    t_dec = t
                    break
            utils.append(min(t_dec+d, T))
        utils = np.array(utils)
        self.assertLess(abs(utils.mean()-h["util"]), 4*utils.std()/np.sqrt(len(utils)))

    def test_scenarios_and_sources(self):
        names = [s["scenario"] for s in m.scenarios()]
        self.assertEqual(len(names), 9)
        self.assertEqual(len(set(names)), 9)
        d = m.load_decisions()
        self.assertEqual(sorted(d.origin.unique()), ["confirmation", "development"])
        self.assertEqual(set(d.policy_id), {f"{b}_D{x}" for b in m.BASES for x in (1, 2)})


if __name__ == "__main__":
    unittest.main()
