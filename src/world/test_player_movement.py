from tile_type import TileType
from tile_map import TileMap
from position import Position
from entities.player import Player

grid = [
    [TileType.WALL, TileType.WALL, TileType.WALL],
    [TileType.WALL, TileType.EMPTY, TileType.WALL],
    [TileType.WALL, TileType.EMPTY, TileType.WALL],
    [TileType.WALL, TileType.WALL, TileType.WALL],
]

world = TileMap(grid)
player = Player(Position(1, 1))

print("Start:", player.position)

player.try_move("DOWN", world)
print("After DOWN:", player.position)

player.try_move("LEFT", world)
print("After LEFT:", player.position)