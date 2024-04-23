import tkinter as tk
from tkinter import simpledialog

print("Witaj w aplikacji zarządzania budżetem")

class Wydatki:
    def __init__(self, przychod, koszt, data, kategoria):
        self.przychod = przychod
        self.koszt = koszt
        self.data = data
        self.kategoria = kategoria

    def wyswietl(self):
       return f"Twój przychód {self.przychod}\nTwój koszt {self.koszt}\nData: {self.data}\nKategoria: {self.kategoria}"

    def oblicz(self):
        wynik = self.przychod - self.koszt
        return wynik

root = tk.Tk()
root.geometry("500x500")
root.withdraw()

lista_wydatkow = []
suma_dochodu = 0
zapytanie = 'y'

while zapytanie.lower() == 'y':
    przychod = float(simpledialog.askstring("Input", "Podaj przychód: "))
    koszt = float(simpledialog.askstring("Input", "Podaj koszt: "))
    data = simpledialog.askstring("Input", "Podaj date DD-MM-YYYY: ")
    kategoria = simpledialog.askstring("Input", "Podaj kategorię: ")
    zapytanie = simpledialog.askstring("Input", "Czy chcesz kontynuować wprowadzanie ?  y/n")

    wydatki_uzytk = Wydatki(przychod, koszt, data, kategoria)
    wydatki_uzytk.wyswietl()

    lista_wydatkow.append(wydatki_uzytk)
    suma_dochodu += wydatki_uzytk.oblicz()

if zapytanie.lower() != "y":
    print("Dziękuję, oto twoje statystyki \n-----------------------------")
    for wydatki_uzytk in lista_wydatkow:
        print(wydatki_uzytk.wyswietl())
        print(f"Twój przychód to: {wydatki_uzytk.oblicz()} zł")
        print("-----------------------------")
    print(f"Suma Twojego dochodu: {suma_dochodu} zł")

root.mainloop()
