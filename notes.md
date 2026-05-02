## Encoding moves:

move = chess.Move.from_uci("e2e4")  
creates Move object from e2 to e4  

move.uci()  
converts back to string  

## To move a piece:

board.push_uci("e2e4") // move the piece from e2 to e4  

## Core loop (bot making a move):

prediction = model(current_state)  
board.push_uci(prediction)  

## Other functions:

board.legal_moves  
// iterable of all legal moves in current position, returns iterator, convert to list to use

board.push(move)  
// applies a Move object to the board (doesnt check legality)

board.pop()  
// undoes the last move

board.parse_uci("e2e4")  
// converts UCI string to Move object (does not apply it)

board.push_uci("e2e4")  
// parses + checks legality + applies move (safest)

board.is_game_over()  
// returns True if game ended (checkmate, stalemate, etc.)

board.result()  
// returns result: "1-0", "0-1", "1/2-1/2", or "*"

board.fen()  
// returns current board state as FEN string