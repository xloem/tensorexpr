from .const import Const as ConstExpr
from . import op as _op
from functools import wraps as _wraps

class ArrayExprMixin:
    def __truediv__(x, y):
        return divide(x, y)
    def __pow__(x, y):
        return pow(x, y)
    def __rtruediv__(y, x):
        return divide(x, y)
    def __rpow__(y, x):
        return pow(x, y)
    #__add__ __sub__ __mul__ __matmul__ __truediv__ __floordiv__ __mod__
    #__divmod__ __pow__ __lshift__ __rshift__ __and__ __xor__ __or__

class ConstArray(ConstExpr, ArrayExprMixin):
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
import inspect

class Op(_op.Op):
    def __init__(self, name):
        func = getattr(array_api, name)
        sig = inspect.signature(func)
        arity = len(sig.parameters)
        super().__init__(name, None, list(range(arity)), [arity])
    def eval(self, x, *ys):
        return getattr(x.__array_namespace__(), self.name)(x, *ys)
    class Expr(_op.Op.Expr, ArrayExprMixin):
        pass

class __ConstConstructorShim:
    def __getattr__(self, name):
        @_wraps(getattr(array_api, name))
        def const(*params, **kwparams):
            val = getattr(array_api, name)(*params, **kwparams)
            return ConstArray(
                val,
                name = f'{name}({",".join([repr(p) for p in params])})',
            )
        globals()[name] = const
class __OpShim:
    def __getattr__(self, name):
        op = Op(name)
        globals()[name] = op

__new = __ConstConstructorShim()
__new.arange
__op = __OpShim()
__op.divide
__op.pow

#abs, acos, acosh, add, all, any, arange, argmax, argmin, argsort, asarray,
#asin, asinh, astype, atan, atan2, atanh, bitwise_and, bitwise_invert,
#bitwise_left_shift, bitwise_or, bitwise_right_shift, bitwise_xor, bool,
#broadcast_arrays, broadcast_to, can_cast, ceil, complex128, complex64, concat,
#conj, cos, cosh, divide, e, empty, empty_like, equal, exp, expand_dims, expm1,
#eye, finfo, flip, float32, float64, floor, floor_divide, from_dlpack, full,
#full_like, greater, greater_equal, iinfo, imag, inf, int16, int32, int64, int8,
#isdtype, isfinite, isinf, isnan, less, less_equal, linalg, linspace, log,
#log10, log1p, log2, logaddexp, logical_and, logical_not, logical_or,
#logical_xor, matmul, matrix_transpose, max, mean, meshgrid, min, multiply, nan,
#negative, nonzero, not_equal, ones, ones_like, permute_dims, pi, positive, pow,
#prod, real, remainder, reshape, result_type, roll, round, sign,sin, sinh, sort,
#sqrt, square, squeeze, stack, std, subtract, sum, take, tan, tanh, tensordot,
#tril, triu, trunc, uint16, uint32, uint64, uint8, unique_all, unique_counts,
#unique_inverse, unique_values, var, vecdot, warnings, where, zeros, zeros_like
