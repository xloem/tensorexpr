class OpGroup:
    def __init__(self, n_total, name=None, ops=[], names = []):
        self.n = n_total
        self.name = name
        self.ops = ops
        self.params = {names[idx] for idx in range(len(names))}
    def __getitem__(self, param):
        return self.params[param] if type(param) is not int else param
class Op:
    def __init__(self, name, group, ins, outs):
        self.name = name
        i
        self.group = group
        self.ins = [self.group[p] for p in ins]
        self.outs = [self.group[p] for p in outs]



