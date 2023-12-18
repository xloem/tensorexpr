from .const import Const as ConstExpr

class ConstArray(ConstExpr):
    def __init__(self, value, name=None):
        super().__init__(value=value)
    # torch
    def float(self):
        #return self.cast(array_api.float32)
        return type(self)(array_api.astype(self.value,array_api.float32), name=self.name)
    # torch
    def to(self, device):
        if device is not None:
            self.value = self.value.to_device(device)
        return self

import numpy.array_api as array_api

class __ConstConstructorShim:
    def __getattr__(self, name):
        import functools
        @functools.wraps(getattr(array_api, name))
        def const(*params, **kwparams):
            val = getattr(array_api, name)(*params, **kwparams)
            return ConstArray(
                val,
                name = f'{name}({",".join([repr(p) for p in params])})',
            )
        globals()[name] = const
__shim = __ConstConstructorShim()
__shim.arange
