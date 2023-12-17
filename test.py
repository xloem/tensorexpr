import torch
from transformers.models.llama import configuration_llama, modeling_llama

config = configuration_llama.LlamaConfig(
    vocab_size = 4,
    hidden_size = 64,
    intermediate_size = 64,
    num_hidden_layers = 2,
    num_attention_heads = 4,
)
model = modeling_llama.LlamaModel(config)
