# Snake Game

A classic Snake game built using Python. The game features both a single-player mode and a two-player competitive mode that introduces mechanics inspired by Tron, where players can collide with each other. This README provides an overview of the game's setup, gameplay, and installation.

## Game Modes
- **Single Player Mode**: Control the snake to collect food and grow as long as possible without colliding with the walls or yourself.
- **Two Player Mode**: Compete against another player! In this mode, each player controls a separate snake, and collisions can occur based on Tron-style mechanics. The collision is managed by tracking the positions of both players' snakes in an array.

## Features
- **Dynamic Gameplay**: The snake's speed increases as you progress.
- **Collision Detection**: Detects wall, self, and in the case of two-player mode, opponent collisions.
- **Score Tracking**: Your score increases as you collect food, and high scores are displayed.
- **Player Control**: Simple controls for each player with adjustable key mappings.

## Requirements
- Python 3.x
- `pygame` library

To install the required packages, use:
```bash
pip install pygame
