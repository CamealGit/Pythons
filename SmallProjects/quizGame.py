print("Welcome to math quizGame")

while True:
    try:
        quest1 = int(input("2+2*2\n1. 2\n2. 6\n3. 1\n4. 8\n"))
        quest2 = int(input("7 power 7\n1. 44\n2. 59\n3. 49\n4. 50\n"))
        quest3 = int(input("256 / 16\n1. 16\n2. 14\n3. 15\n4. 19\n"))
        quest4 = int(input("11 power 11\n1. 121\n2. 144\n3. 131\n4. 110\n"))
        score = 0
        if quest1 == 6:
            score += 1
        if quest2 == 49:
            score += 1
        if quest3 == 16:
            score += 1
        if quest4 == 121:
            score += 1
        print(f"Your total score is {score} / 4")
        break
    except ValueError:
        print("Wrong value !!!")

