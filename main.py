# Play the game
import chess
from tokenizer import Tokenizer

# return all current legal move ids of a current board position
def legal_moves(board: chess.Board, tokenizer: Tokenizer) -> list[int]:
    ids = []
    legal = list(board.legal_moves)
    
    for move in legal:
        move = move.uci()
        ids.append(tokenizer.encode(move))

    return ids

if __name__ == "__main__":
    board = chess.Board()
    tokenizer = Tokenizer()

    ids = legal_moves(board, tokenizer)

    print(ids)
    print(len(ids))