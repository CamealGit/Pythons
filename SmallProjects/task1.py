def dodaj(a, b):
    return f"Twoj wynik to {a + b}"

def odejmij(a, b):
    return f"Twoj wynik to {a - b}"

def pomnoz(a, b):
    return f"Twój wynik to {a * b}"

def podziel(a, b):
    try:
        return f"Twoj wynik to {a / b}"
    except ZeroDivisionError:
        print("Nie dziel przez zero")

def poteguj(a, b):
    return f"Twoj wynik to {pow(a, b)}"

