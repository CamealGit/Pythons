import sys

print("Wybierz opcje\n1 - dodawanie, 2 - odejmowanie\n3 - mnozenie, 4 - dzielenie\n5 - zakończ")
choice = int(input("Twój wybór -> "))
if choice == 5:
    sys.exit()
a = int(input("Wpisz pierwszą wartosc: "))
b = int(input("Wpisz drugą wartosc: "))
def dodawanie():
    return a + b
def odejmowanie():
    return a - b
def mnozenie():
    return a * b
def dzielenie():
    try:
        wynik = a / b
        return f"Twoja liczba to: {wynik}"
    except ZeroDivisionError:
        return "Nie dzielimy przez zero!"

while True:
    if choice == 1:
        print("Twoja liczba to", dodawanie())
        break
    elif choice == 2:
        print("Twoja liczba to", odejmowanie())
        break
    elif choice == 3:
        print("Twoja liczba to", mnozenie())
        break
    elif choice == 4:
        print(dzielenie())
        break
