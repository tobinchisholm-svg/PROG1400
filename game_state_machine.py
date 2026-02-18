from enum import Enum, auto


class GameState(Enum):
    MENU = auto()
    PLAYING = auto()
    PAUSED = auto()
    FOOD_EATEN = auto()
    GAME_OVER = auto()


class SnakeGame:
    """
    Original state machine class (unchanged).
    """

    def __init__(self):
        self.state = GameState.MENU
        print("Game started. State = MENU")

    # ------------------------------
    # State Machine Update Loop
    # ------------------------------
    def update(self):
        """Runs once per frame/tick. Shows what the game is doing in this state."""
        if self.state == GameState.MENU:
            print("MENU: Waiting for player input... (startSelected / exitGame)")

        elif self.state == GameState.PLAYING:
            print("PLAYING: Snake is moving... (pausePressed / ateApple / collidedWithWallOrSelf)")

        elif self.state == GameState.PAUSED:
            print("PAUSED: Game is frozen. (pausePressed to resume)")

        elif self.state == GameState.FOOD_EATEN:
            print("FOOD_EATEN: Growing snake, spawning apple, updating score...")
            self.grow_snake_spawn_apple_update_score()

        elif self.state == GameState.GAME_OVER:
            print("GAME_OVER: Showing score. (restart to return to MENU)")

    # ------------------------------
    # TRANSITIONS (UML arrows)
    # ------------------------------

    def start_game(self):
        self.state = GameState.MENU
        print("Transition → MENU")

    def start_selected(self):
        self.state = GameState.PLAYING
        print("Transition → PLAYING")

    def exit_game(self):
        print("Exiting game...")

    def pause_pressed(self):
        if self.state == GameState.PLAYING:
            self.state = GameState.PAUSED
            print("Transition → PAUSED")
        elif self.state == GameState.PAUSED:
            self.state = GameState.PLAYING
            print("Transition → PLAYING")

    def ate_apple(self):
        if self.state == GameState.PLAYING:
            self.state = GameState.FOOD_EATEN
            print("Transition → FOOD_EATEN")

    def grow_snake_spawn_apple_update_score(self):
        print("  - Growing snake")
        print("  - Spawning new apple")
        print("  - Updating score")
        self.state = GameState.PLAYING
        print("Transition → PLAYING")

    def collided_with_wall_or_self(self):
        if self.state == GameState.PLAYING:
            self.state = GameState.GAME_OVER
            print("Transition → GAME_OVER")

    def collision_normal(self):
        self.collided_with_wall_or_self()

    def restart(self):
        self.state = GameState.MENU
        print("Transition → MENU")


# -----------------------------------------------------
# Wrapper class so your code works EXACTLY as requested
# -----------------------------------------------------
class GameStateMachine(SnakeGame):
    """
    This class exists ONLY so your runner code works exactly
    without changing the original SnakeGame class.
    """
    pass


# -----------------------------------------------------
# EXACTLY the block you asked to add (UNCHANGED)
# -----------------------------------------------------
if __name__ == "__main__":
    gsm = GameStateMachine()

    # MENU -> PLAYING
    gsm.start_selected()
    gsm.update()

    # PLAYING -> PAUSED
    gsm.pause_pressed()
    gsm.update()

    # PAUSED -> PLAYING
    gsm.pause_pressed()
    gsm.update()

    # PLAYING -> GAME_OVER
    gsm.collision_normal()
    gsm.update()

    # GAME_OVER -> MENU
    gsm.restart()
    gsm.update()