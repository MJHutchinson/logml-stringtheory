import torch.nn as nn


from torch import nn
import math


def mlp(
    n_input,
    n_output,
    n_hidden,
    activations=None,
    input_activation=None,
    final_activation=None,
    weight_init=None,
):
    if activations is None:
        activations = len(n_hidden) * [nn.ReLU()]
    elif isinstance(activations, nn.Module):
        activations = len(n_hidden) * [activations]

    layer_dimensions = [n_input] + n_hidden + [n_output]
    layers = []

    if input_activation is not None:
        layers.append(input_activation)

    for i in range(len(layer_dimensions) - 2):
        layers.append(nn.Linear(layer_dimensions[i], layer_dimensions[i + 1]))
        layers.append(activations[i])

    layers.append(nn.Linear(layer_dimensions[-2], layer_dimensions[-1]))

    if final_activation is not None:
        layers.append(final_activation)

    net = nn.Sequential(*layers)

    if weight_init is not None:
        for m in net:
            weight_init(m)

    return net


def xavier_init(m):
    if isinstance(m, (nn.Linear, nn.Conv2d)):
        nn.init.xavier_normal_(m.weight)
        if m.bias is not None:
            m.bias.data.fill_(0)

    elif isinstance(m, (nn.BatchNorm1d, nn.BatchNorm2d)):
        m.weight.data.fill_(1)
        if m.bias is not None:
            m.bias.data.fill_(0)


def truncated_normal_init(m):
    if isinstance(m, (nn.Linear, nn.Conv2d)):
        truncated_normal(m.weight, mean=0, std=1 / math.sqrt(m.weight.shape[1]))
        if m.bias is not None:
            m.bias.data.fill_(0)

    elif isinstance(m, (nn.BatchNorm1d, nn.BatchNorm2d)):
        m.weight.data.fill_(1)
        if m.bias is not None:
            m.bias.data.fill_(0)


def truncated_normal(tensor, mean, std):
    # https://discuss.pytorch.org/t/implementing-truncated-normal-initializer/4778/15
    size = tensor.shape
    tmp = tensor.new_empty(size + (4,)).normal_()
    valid = (tmp < 2) & (tmp > -2)
    ind = valid.max(-1, keepdim=True)[1]
    tensor.data.copy_(tmp.gather(-1, ind).squeeze(-1))
    tensor.data.mul_(std).add_(mean)
    return tensor
