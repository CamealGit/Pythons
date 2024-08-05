class Samochod:
    def __init__(self):
        self.marka = ""
        self.model = ""
        self.rok_produkcji = 0
        self.przebieg = 0

    def przebieg_update(self, liczba_kilometrow):
        updated = self.przebieg + liczba_kilometrow
        self.przebieg = updated
        return updated

    def dane(self):
        while True:
            self.marka = input("Wpisz marke samochodu: ")
            if self.marka.isalpha():
                break
            else:
                print("Wpisano złą wartość")

        while True:
            self.model = input("Wpisz model samochodu: ")
            if self.model.isalpha():
                break
            else:
                print("Wpisano złą wartość")

        while True:
            try:
                self.rok_produkcji = int(input("Wpisz rok produkcji: "))
                if 2024 >= self.rok_produkcji >= 1950:
                    break
            except ValueError:
                print("Wpisano złą wartość, Spróbuj ponownie")

        while True:
            try:
                self.przebieg = int(input("Wpisz przebieg: "))
                if self.przebieg > 0:
                    break
            except ValueError:
                print("Wpisano złą wartość")

        return f"{self.marka} | {self.model} | {self.rok_produkcji} | {self.przebieg} km"

samochodzik = Samochod()
print(samochodzik.dane())
