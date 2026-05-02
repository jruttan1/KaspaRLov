import torch
import torch.nn as nn

class Model(nn.Module):
    # define the layers
    def __init__(self, vocab_size: int, d_model: int): # initialize parent (nn.Module)
        super().__init__()

        self.token_embedding = nn.Embedding(vocab_size, d_model) # embedding layer (move_id -> learnable vector)
        #rows = vocab_size, 4032 possible moves
        #columns = d_model, learnable parameters (hyperparameter = 64)
        self.output_layer = nn.Linear(d_model, vocab_size)

    # define forward pass (how data flows through nn)
    # input_ids -> token_embedding -> output_layer -> logits

    # shape of input:
    # [x,y] = [batch_size, 3 moves in sequence]
    # then ->
    # shape of output of embedding layer:
    # [x,y,z] = [batch_size, # moves in sequence, d_model]
    # batch size = number of examples processed simultaneously
    def forward(self, input_ids): 
        x = self.token_embedding(input_ids) # ids to vectors
        logits = self.output_layer(x) # vectors to scores over all ids
        return logits
    
if __name__ == "__main__":
    model = Model(vocab_size=4032, d_model=64)

    input_ids = torch.tensor([[2113, 1601, 3066]])

    logits = model(input_ids)

    print(logits.shape)