from . import functional

from tensorexpr import Const

class Module:
    pass
class ReLU:
    pass
class ReLU6:
    pass
class Sigmoid:
    pass
class Tanh:
    pass
class BCEWithLogitsLoss:
    pass
class CrossEntropyLoss:
    pass
class MSELoss:
    pass
class ModuleList:
    def __init__(self, modules):
        pass
class Linear:
    def __init__(self, input_size, output_size, bias=True):
        self.weight = Const(
            name = "Linear.weight",
            shape = [input_size,output_size],
        )
        if bias:
            self.weight = Const(
                name = "Linear.bias",
                shape = [output_size,],
            )
class Embedding:
    def __init__(self, vocab_size, hidden_size, padding_idx):
        self.weight = [
            Const(
                name = f'Embedding.weight[{idx}]',
                shape = [hidden_size,],
            )
            for idx in range(vocab_size)
        ]
class LayerNorm:
    pass

