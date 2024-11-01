# Snake Game

This is a simple but engaging snake game built using Python and the Pygame library, designed with both single-player and two-player modes. Players control a snake that grows in length as it eats apples, avoiding walls and, in two-player mode, the opponent's snake as well. The two-player adaptation provides a unique competitive twist.

## How to Play
- **Single Player Mode**: Control your snake with arrow keys to eat apples that randomly appear on the screen. Each apple consumed will make your snake grow longer. Avoid hitting the walls or yourself to keep playing!
- **Two Player Mode**: Compete against another player! Each player controls their own snake, avoiding collisions with walls, their own body, and the other player’s snake. Collisions are tracked in an array for both players, enabling detection of wall, self, and opponent collisions.

### Controls
- **Single Player**:
  - Arrow Keys: Move the snake.
- **Two Player**:
  - Player 1: Arrow keys.
  - Player 2: WASD keys.

## Features
- **Random Apple Generation**: Apples appear at random locations on the screen after each one is eaten.
- **Two Player Mode**: Each player controls a separate snake in a competitive mode with collision detection based on the "Tron" mechanic. The game ends if either player collides with a wall, themselves, however, when a head collides with a tail or body that is part of the opponent's body that section will be cut off.
- **Game Menu**: A main menu allows you to select single-player, two-player, or exit the game.

## Requirements
- Python 3.x
- `pygame` library

To install the required packages, use:
```bash
pip install pygame
