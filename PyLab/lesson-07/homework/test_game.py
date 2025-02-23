from __future__ import annotations

"""

1. Suppose you are on branch `tmp`, commit the current changes:

git add .
git commit -m "Update to tmp; I will delete branch tmp soon"

2. Switch to branch `main`, and reset to old commit, and pull the new commit from github:

git swith branch main
git reset --hard 6a7d757daa08855db8cc44a6927f5b38b596c718
git pull origin main

3. Create and switch to a new branch `homework/07-<github-username>`

git branch homework/07-<github-username>
git switch homework/07-<github-username>

4. Implement the homework.

5. Add, commit, push (to create a new branch on github).

git add .
git commit -m "Update Homework from <github-user-name>"
git push origin homework/07-<github-username>

6. PR on github.

"""


from pylab.games import Game, DiceGame, GuessNumberGame
from pylab.utils import load_game_configs_from_json, convert_keys


class GameContainerIterator:
    def __init__(self, game_container: GameContainer):
        self.container: GameContainer = game_container
        self.cursor: int = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor < len(self.container.games):
            element = self.container.games[self.cursor]
            self.cursor = self.cursor + 1
            return element
        raise StopIteration


class GameContainer:
    def __init__(self, games: list[Game]):
        self.games: list[Game] = games

    def __iter__(self):
        return GameContainerIterator(self)

    def __iadd__(self, element):
        """
        container += game
        """
        if not isinstance(element, Game):
            raise TypeError("The element must be a Game instance")
        # Implement me.
        # Append the element into games


def main():
    json_path = "./lesson-07/homework/game_config.json"
    configs: list[dict] = load_game_configs_from_json(json_path=json_path)

    container: GameContainer = GameContainer([])

    for cfg in configs:
        cfg: dict = convert_keys(cfg)
        # Implement me.
        # Create a game.
        game: Game = ...
        container += game  # This calls GameContainer.__iadd__

    for game in container:
        # Run the game.
        game.run()


if __name__ == "__main__":
    main()
