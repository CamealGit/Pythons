from datetime import datetime

class Samochod:
    def __init__(self, marka, model, rok_produkcji, przebieg):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg

    def przebieg_update(self, liczba_kilometrow):
        updated = self.przebieg + liczba_kilometrow
        self.przebieg = updated
        return updated

    def dane(self):
        self.marka = input("Wpisz marke samochodu: ")
        self.model = input("Wpisz model samochodu: ")
        while True:
            try:
                self.rok_produkcji = input("Wpisz rok produkcji: ")
                int(self.rok_produkcji)
                break
            except ValueError:
                print("Wpisano złą wartość")

        self.przebieg = int(input("Wpisz przebieg: "))
        return f"{self.marka} | {self.model} | {self.rok_produkcji} | {self.przebieg} km"

samochodzik = Samochod("Ford", "Mustang", 2018, 30000)
print(samochodzik.dane())
