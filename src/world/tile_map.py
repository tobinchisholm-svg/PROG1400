# tile_map.py
from typing import List, Sequence, Protocol
import random
from tile_type import TileType
from position import Position


class WalkabilityPolicy(Protocol):
    """Strategy interface for deciding whether a tile can be stepped into."""
    def is_walkable(self, tile: TileType) -> bool: ...


class SnakeWalkability:
    """
    Default Snake rule:
      - Can move into EMPTY or FOOD
      - Cannot move into WALL or SNAKE_BODY
    """
    def is_walkable(self, tile: TileType) -> bool:
        return tile in (TileType.EMPTY, TileType.FOOD)


class TileMap:
    """Immutable-size 2D grid with bounds checking and walkability."""
    __slots__ = ("_grid", "_rows", "_cols", "_policy")

    def __init__(
        self,
        grid: Sequence[Sequence[TileType]],
        policy: WalkabilityPolicy | None = None,
    ) -> None:

        if not grid:
            raise ValueError("grid must have at least one row")
        row_lengths = {len(row) for row in grid}
        if len(row_lengths) != 1:
            raise ValueError("grid must be rectangular")

        self._rows = len(grid)
        self._cols = len(grid[0])

        self._grid: List[List[TileType]] = [list(row) for row in grid]
        self._policy: WalkabilityPolicy = policy or SnakeWalkability()

    # ---------------------------
    # Dimensions & bounds
    # ---------------------------
    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    def in_bounds(self, pos: Position) -> bool:
        return 0 <= pos.row < self._rows and 0 <= pos.col < self._cols

    # ---------------------------
    # Tile accessors
    # ---------------------------
    def get_tile(self, pos: Position) -> TileType:
        if not self.in_bounds(pos):
            return TileType.WALL
        return self._grid[pos.row][pos.col]

    def set_tile(self, pos: Position, tile: TileType) -> None:
        if not self.in_bounds(pos):
            raise IndexError(f"Position out of bounds: {pos}")
        self._grid[pos.row][pos.col] = tile

    # ---------------------------
    # Walkability
    # ---------------------------
    def is_walkable(self, pos: Position) -> bool:
        return self._policy.is_walkable(self.get_tile(pos))

    # ---------------------------
    # Convenience
    # ---------------------------
    def render(self) -> str:
        return "\n".join("".join(cell.value for cell in row) for row in self._grid)


# ----------------- Classic Snake Board: 20x20, border walls only -----------------
if __name__ == "__main__":
# Make a fully empty board (20x20)
    rows, cols = 20, 20

    grid = []   # this will become a list of rows

    for r in range(rows):           # go through each row
        row = []                    # start a new empty row
        for c in range(cols):       # go through each column
            row.append(TileType.EMPTY)   # put an EMPTY tile in this cell
        grid.append(row)            # add the completed row to the grid
    print(grid)
    # Add BORDER walls only
 # Add BORDER walls only (beginner‑friendly version)

# Top row
    for c in range(cols):
        grid[0][c] = TileType.WALL

    # Bottom row
    for c in range(cols):
        grid[rows - 1][c] = TileType.WALL

    # Left column
    for r in range(rows):
        grid[r][0] = TileType.WALL

    # Right column
    for r in range(rows):
        grid[r][cols - 1] = TileType.WALL

    # Random apple placement (inside empty area)
    empty_cells = [
        (r, c)
        for r in range(1, rows - 1)
        for c in range(1, cols - 1)
    ]
    food_r, food_c = random.choice(empty_cells)
    grid[food_r][food_c] = TileType.FOOD

    # Build the world
    world = TileMap(grid)
    print(world.render())

    # Sanity checks
    print("in_bounds(1,1):", world.in_bounds(Position(1, 1)))
    print("food placed at:", food_r, food_c)
    print("food tile:", world.get_tile(Position(food_r, food_c)))
    print("is_walkable(food):", world.is_walkable(Position(food_r, food_c)))