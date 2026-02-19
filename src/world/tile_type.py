
from enum import Enum

class TileType(Enum):
    EMPTY = "."        # empty cell where the snake can move
    WALL = "#"         # boundary or obstacle
    SNAKE_HEAD = "@"   # head of the snake (distinct for clarity)
    SNAKE_BODY = "o"   # body segments
    FOOD = "*"         # food to grow the snake
