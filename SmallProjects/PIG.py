import random

player1score = 0
player2score = 0
total = 0


def player2turn():
    global player2score, total
    print("Player 2's turn: ")
    question = input("Roll dice? y/n ")
    if question.lower() == "y":
        number = random.randint(1, 6)
        print(f"Random number is {number}")
        if number != 1:
            player2score += number
        else:
            player2score = 0
            print("Failed, your total score now is 0")
        print(f"Player 2's current total score is {player2score}")
        total = player2score
    elif question.lower() == "n":
        print(f"Player 2 saves a score of {player2score}")

    if total < 25:
        player1turn()
    else:
        print("Player 2 won !")


def player1turn():
    global player1score, total
    print("Player 1's turn: ")
    question = input("Roll dice? y/n ")
    if question.lower() == "y":
        number = random.randint(1, 6)
        print(f"Random number is {number}")
        if number != 1:
            player1score += number
        else:
            player1score = 0
            print("Failed, your total score now is 0")
        print(f"Player 1's current total score is {player1score}")
        total = player1score
    elif question.lower() == "n":
        print(f"Player 1 saves a score of {player1score}")

    if total < 25:
        player2turn()
    else:
        print("Player 1 won!")


player1turn()
