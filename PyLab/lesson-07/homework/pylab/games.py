import abc
from abc import ABC


class Game(ABC):
    def __init__(self, game_type: str, round: int = 1):
        self.game_type = game_type
        self.round = round

    @abc.abstractmethod
    def _run_one_round(self):
        pass

    def run(self):
        print(f"Game Type: {self.game_type}, Round: {self.round}")
        for _ in range(self.round):
            self._run_one_round()


class DiceGame(Game):
    """
    @see "lesson-02/src/dice_game.py"
    """

    def __init__(self, game_type: str, round: int = 1):
        # Implement me.
        pass

    def _run_one_round(self):
        # Implement me.
        pass


class GuessNumberGame(Game):
    """
    @see "lesson-02/src/guess_number_v2.py"
    """

    def __init__(self, game_type: str, round: int = 1):
        # Implement me.
        pass

    def _run_one_round(self):
        # Implement me.
        pass


def __test(game: Game):
    game._run_one_round()


if __name__ == "__main__":
    __test(DiceGame("dice", 2))
    __test(GuessNumberGame("guessnumber", 2))
