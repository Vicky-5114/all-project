import random


def guess_number():
    left = 1
    right = 100
    while True:
        print("I have generated a number.")
        random_number = (left + right) // 2
        print("I have guessed " + str(random_number))
        result = input("Large or Small?")
        if result == "Large":
            right = random_number - 1
        elif result == "Small":
            left = random_number + 1
        else:
            break
        print(f"New left and right: [{left}, {right}]")


if __name__ == "__main__":
    guess_number()
