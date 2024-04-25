import time
import random

# class TextLoad:
#     def __init__(self, difficulty):
#         self.difficulty = difficulty


# difficulty = int(input("Wybierz poziom trudności: "))
#
# if difficulty == 1:
#     file = open('text1', 'r')
#     print(file.read(50))
# elif difficulty == 2:
#     file = open('text2', 'r')
#     print(file.read(94))
# elif difficulty == 3:
#     file = open('text3', 'r')
#     print(file.read(132))


start = input("Gdy wpiszesz y to zacznie sie gierka: ")
print(start)

seconds = 3
for i in range(1, seconds):
    print(f"Odliczanie {i}")
    time.sleep(1)
print("koniec odliczania")





# plik = open('texts', 'r')
# print(plik.read())
# print(type(plik))



