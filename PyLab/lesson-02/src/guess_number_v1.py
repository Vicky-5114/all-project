import random


def guess_number():
    random_number = random.randint(1, 100)
    print("I have generated a number.")

    while True:
        user_guessed_number = int(input("Please guess a number: "))
        print(user_guessed_number)
        if user_guessed_number > random_number:
            print("Too large!")
        elif user_guessed_number < random_number:
            print("Too small!")
        else:
            print("You are correct!")
            break


if __name__ == "__main__":
    guess_number()
