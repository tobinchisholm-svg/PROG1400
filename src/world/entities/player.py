from position import Position

DIRECTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}

class Player:
    def __init__(self, start_pos: Position):
        self.position = start_pos

    def get_next_position(self, direction: str) -> Position:
        dr, dc = DIRECTIONS[direction]
        return Position(
            self.position.row + dr,
            self.position.col + dc
        )

    def try_move(self, direction: str, tile_map) -> bool:
        next_pos = self.get_next_position(direction)
        if tile_map.is_walkable(next_pos):
            self.position = next_pos
            return True
        return False