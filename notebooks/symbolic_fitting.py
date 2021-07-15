# %%
%load_ext autoreload
%autoreload 2

import os
import numpy as np
import pandas as pd
import seaborn as sns
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader, random_split
from pysr import pysr, best
import matplotlib.pyplot as plt

from stringml.data import (
    get_geometry_ids,
    load_vector_bundle_solutions_npy,
    reduce_solutions,
    flatten_solutions,
    generate_negative_data_reduced
)
from stringml.mlp import mlp

os.chdir("/data/ziz/not-backed-up/mhutchin/logml-stringtheory")

# %%
ids = get_geometry_ids()
positive_data = load_vector_bundle_solutions_npy(7862)
positive_data = flatten_solutions(reduce_solutions(positive_data))
negative_data = generate_negative_data_reduced(positive_data.shape[0], positive_data)
data = np.concatenate([positive_data, negative_data])
labels = np.concatenate([np.ones(positive_data.shape[0]), np.zeros(negative_data.shape[0])])
# %%
net = mlp(data.shape[1], 1, [5, 5])
# %%
test_train_split = 0.5
batch_size = 32

dataset = TensorDataset(
    torch.Tensor(data).to(torch.float32),
    torch.Tensor(labels)
)
train_size = int(len(dataset) * test_train_split)
test_size = len(dataset) - train_size
split_datasets = random_split(dataset, [train_size, test_size])
train_loader = DataLoader(split_datasets[0], batch_size=batch_size, shuffle=True)
test_loader = DataLoader(split_datasets[1], batch_size=batch_size, shuffle=True)

# %%
def train_epoch(model, dataloader, opt, criteria):
    model.train()
    losses = []
    for X, y in dataloader:
        opt.zero_grad()
        output = model(X)
        loss = criteria(output.squeeze(1), y)
        loss.backward()
        opt.step()
        losses.append(loss.data.numpy())
    return losses

def binary_logit_classification_accuracy(model, dataloader):
    model.eval()
    with torch.no_grad():
        correct = 0
        for X, y in dataloader:
            logits = model(X)
            predictions = logits.squeeze(1) > 0
            correct += (predictions == y).sum()
        return float(correct) / float(len(dataloader.dataset)) 

# %%
optimiser = optim.Adam(net.parameters(), 1e-3)
epochs = 20

losses = []
test_acc = []
train_acc = []
for e in range(epochs):
    print(e)
    epoch_losses = train_epoch(net, train_loader, optimiser, nn.BCEWithLogitsLoss())
    losses += epoch_losses
    test_acc.append(binary_logit_classification_accuracy(net, test_loader))
    train_acc.append(binary_logit_classification_accuracy(net, train_loader))

# %%
plt.plot(losses)
# %%

plt.plot(train_acc, label='Train accuracy')
plt.plot(test_acc, label='Test accuracy')
plt.legend()

# %%
X = data
y_label = labels
with torch.no_grad():
    y_logit = net(torch.Tensor(data).to(torch.float32)).squeeze().numpy()
    y_prob = nn.Sigmoid()(net(torch.Tensor(data).to(torch.float32)).squeeze()).numpy()

dataframe = pd.DataFrame(data={
    'label': y_label,
    'logit': y_logit,
    'prob': y_prob,
})
# %%
sns.histplot(data=dataframe, x='prob', hue='label', bins=100)
# %%
sns.histplot(data=dataframe, x='logit', hue='label', bins=100)
# %%
equations_probs = pysr(
    X, y_prob,
    batching=True
)
# %%
