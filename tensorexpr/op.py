from . import array_api
from .expr import Expr as _Expr

class OpGroup:
    def __init__(self, n_total, name=None, ops=[], names = []):
        self.n = n_total
        self.name = name
        self.ops = ops
        self.params = {names[idx] for idx in range(len(names))}

class Op:
    def __init__(self, name, group, ins, outs):
        self.name = name
        self.group = group
        idcs = array_api.array_api.asarray([
            self.group.params[p]
                if type(p) is not int
                else p
            for p in ins + outs
        ])
        self.ins = idcs[:len(ins)]
        self.outs = idcs[len(ins):]
        if self.group is not None:
            self.group.ops.append(self)
    def __call__(self, *ins):
        return self.Expr(self, *ins)
    def eval(self, *ins):
        raise NotImplementedError(type(self), self.name)
    class Expr(_Expr):
        def __init__(self, op, *operands):
            self.op = op
            self.ins = operands
        def eval(self):
            return self.op.eval(*[
                x.eval() for x in self.ins
            ])
