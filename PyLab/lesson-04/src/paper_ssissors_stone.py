import random


def paper_scissors_stone():
    winning_condition = {"paper": "stone", "scissors": "papaer", "stone": "scissors"}
    options = list(winning_condition.keys())

    while True:
        # random_number = random.randint(0, 2)
        # computer_choice = winning_condition[random_number]
        computer_choice: str = random.choice(options)

        user_choice = input("Please enter [paper/scissors/stone]: ")

        if user_choice not in options:
            print("Invalid input")
            break

        if user_choice == computer_choice:
            print("draw")
        elif winning_condition[user_choice] == computer_choice:
            print("win")
        else:
            print("lose")


paper_scissors_stone()
