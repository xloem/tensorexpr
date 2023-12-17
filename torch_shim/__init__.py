__version__ = "0.0.0"
from . import device, distributed

import sys
if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata
_imversion = importlib_metadata.version
def __imversion(spec):
    if spec == "torch":
        return __version__
    else:
        return _imversion(spec)
importlib_metadata.version = __imversion

class dtype:
    pass
dtype = type
float = __builtins__['float']
Size = list
class Tensor:
    pass
FloatTensor = Tensor
LongTensor = Tensor
BoolTensor = Tensor

import contextlib
@contextlib.contextmanager
def no_grad():
    yield
def save():
    pass
