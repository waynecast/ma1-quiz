class Bank:
    def __init__(self):
        self.Q = []
    def add(self, t, q, a, w, e, s, f=False):
        assert len(w) == 3, q
        assert a not in w, q
        assert len(set(w)) == 3, q
        self.Q.append({"topic": t, "q": q, "a": a, "w": w, "e": e, "s": s, "f": f})
