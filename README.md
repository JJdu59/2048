# 2048
A minimalist recreation of the classic 2048 puzzle game using Python and Pygame.

## 🧩 Gameplay
- Move tiles using:
Z = Up, S = Down, Q = Left, D = Right (AZERTY layout)
(Modify to WASD if using QWERTY)

- Combine identical numbers to create higher tiles.

- The goal is to reach 2048 — or go even further!

- The game ends when no moves are left.

## Prerequisites
- Pygame installed

## 🛠️ How It Works
- 4×4 grid represented by a 2D list.

- On every valid move, a new tile (2 or 4) spawns randomly.

- Combines same-value adjacent tiles.

- Score is computed and highscore is tracked via `highscore.txt`.
