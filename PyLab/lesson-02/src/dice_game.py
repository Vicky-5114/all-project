import random


def roll_dice() -> int:
    dice = random.randint(1, 6)
    return dice


def game():
    computer_dice = roll_dice()
    user_input = input("Input y to continue: ")
    if user_input != "y":
        return
    user_dice = roll_dice()
    print(f"Your dice: {user_dice}")
    guess = input("Your is larger or smaller? ")

    if (guess == "larger" and user_dice > computer_dice) or (
        guess == "smaller" and user_dice < computer_dice
    ):
        print("You win")
    else:
        print("You lose")


if __name__ == "__main__":
    game()
