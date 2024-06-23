import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x / torch.sum(exp_x)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        max_x = torch.max(x)
        exp_x = torch.exp(x - max_x)
        return exp_x / torch.sum(exp_x)


# Test with a sample input
input_tensor = torch.tensor([1, 2, 300000000])

# Using Softmax
softmax = Softmax()
output_softmax = softmax(input_tensor)
print("Softmax Output:", output_softmax)

# Using SoftmaxStable
softmax_stable = SoftmaxStable()
output_softmax_stable = softmax_stable(input_tensor)
print("Softmax Stable Output:", output_softmax_stable)
