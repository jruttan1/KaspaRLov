# KaspaRLov

A human-like chess bot trained on low elo games with the goal of replicating humanistic play patterns for players around 500-800 Elo. Not designed to be the best, but to feel like playing against another human

The first version uses supervised next move prediction from PGN move sequences. Moves are encoded as UCI tokens, passed through a small GPT transformer, filtered through a legal-move mask with `python-chess`, and sampled to produce playable moves.

The project will later be integrated into my portfolio site as an interactive ML system. Visitor games and feedback will be collected to tune the bot's behavior over time, with reinforcement learning as a possible future direction.

Inspired by concepts from [ChessGPT, NeurIPS '23](https://arxiv.org/abs/2306.09200), mainly modelling chess games as move sequences for next token prediction.

## Setup

```bash
source .venv/bin/activate
