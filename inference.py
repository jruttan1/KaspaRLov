# Play the game
import chess
from tokenizer import Tokenizer
import torch

def bot_move(board, move_history, model, tokenizer):

    # build a full move sequence up to a certain board state
    if len(move_history) == 0:
        history_ids = [tokenizer.encode(tokenizer.start_token)]
    else:
        history_ids = [tokenizer.encode(move) for move in move_history]


    # convert input to a tensor
    input_tensor = torch.tensor(history_ids)

    # run model prediction without training 
    model.eval()

    with torch.no_grad():
        logits = model(input_tensor)
    
    # take logits for next position (prediction)
    next_logits = logits[0, -1]

    # Mask illegal moves
    mask = mask_illegal(board, tokenizer)
    masked_logits = next_logits.masked_fill(~mask, float("-inf"))

    # Softmax
    chosen_move = softmax(masked_logits)

    # Make move on board
    board.push_uci(chosen_move)

    # Save move in sequence
    move_history.append(chosen_move)


# return all current legal move ids of a current board position
def legal_moves(board: chess.Board, tokenizer: Tokenizer) -> list[int]:
    ids = []
    legal = list(board.legal_moves)
    
    for move in legal:
        move = move.uci()
        ids.append(tokenizer.encode(move))

    return ids

# mask illegal moves
def mask_illegal(board: chess.Board, tokenizer: Tokenizer) -> list[bool]:
    vocab_size = len(tokenizer.uci_to_idx)
    mask = torch.zeros(vocab_size, dtype=torch.bool) # intialize a last of False * vocab_size
    legal_ids = legal_moves(board, tokenizer)
    for move_id in legal_ids:
        mask[move_id] = True
    
    return mask


# softmax
def softmax(logits):
    masked_logits = mask_illegal(logits)
    probs = torch.softmax(masked_logits, dim=-1)
    move_id = torch.multinomial(probs, num_samples=1).item()

    return move_id


if __name__ == "__main__":
    board = chess.Board()
    tokenizer = Tokenizer()

    ids = legal_moves(board, tokenizer)

    print(ids)
    print(len(ids))