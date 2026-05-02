import torch
import torch.nn as nn

from model import Model
from tokenizer import Tokenizer

# input_ids -> model -> logits -> loss -> backward -> optimizer step

# hyperparameters
d_model = 64
learning_rate = 0.001
epochs = 100

# init
tokenizer = Tokenizer()
vocab_size = len(tokenizer.uci_to_idx)
model = Model(vocab_size, d_model)

# data - will come from real dataset when i have wifi
moves = ["e2e4", "e7e5", "g1f3", "b8c6"] #mock data for now
ids = [tokenizer.encode(move) for move in moves]

# when lined up, input[i] predicts target[i]
input_ids = ids[:-1] # shift right 1
target_ids = ids[1:] # shift left 1

input_tensor = torch.tensor([input_ids])
target_tensor = torch.tensor([target_ids])


# training loop
for epoch in range(epochs):
    logits = model(input_tensor)

    loss_fn = nn.CrossEntropyLoss() # cross entropy loss function from torch
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate) # class for updating learnable parameters

    loss = loss_fn(
        logits.view(-1, vocab_size),
        target_tensor.view(-1)
        )
    
    optimizer.zero_grad() # zero the grads
    loss.backward() # compute backward pass gradients
    optimizer.step() 

    # print loss every 10 epochs
    if epoch % 10 == 0:
        print(epoch, loss.item())