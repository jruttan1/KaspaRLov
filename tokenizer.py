# Convert chess moves to ids and back: encode(uci) -> id, decode(id) -> uci

class Tokenizer:

    def __init__(self):
        self.uci_to_idx = {}
        self.idx_to_uci = {}
        self.start_token = "<START>"


        def build():
            squares = []
            moves = []
            ranks = "12345678"
            files = "abcdefgh"

            for file in files:
                for rank in ranks:
                    squares.append(file+rank)
        
            for from_square in squares:
                for to_square in squares:
                    if from_square != to_square:
                        moves.append(from_square+to_square)

            return [self.start_token] + moves

        moves = build()

        # build maps
        for i, move in enumerate(moves):
            self.uci_to_idx[move] = i
            self.idx_to_uci[i] = move



            
    # Take in dictionaries and a string and return its ID
    def encode(self, uci: str) -> int:
        return self.uci_to_idx[uci]


    def decode(self, idx: int) -> str:
        return self.idx_to_uci[idx]


if __name__ == "__main__":
    tokenizer = Tokenizer()

    move_id = tokenizer.encode("e2e4")
    print(move_id)

    for uci, idx in list(tokenizer.uci_to_idx.items())[:15]:
        print(uci, idx)

        