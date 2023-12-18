from .expr import Expr

class Const(Expr):
    def __init__(self, value = None, name = None, shape = None, dtype = None):
        self.name = name
        self.value = value
        if value is not None:
            shape = value.shape
            dtype = value.dtype
        self.shape = shape
        self.dtype = dtype


