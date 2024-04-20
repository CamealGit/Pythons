import tkinter as tk
from tkinter import simpledialog

print("Witaj w aplikacji zarządzania budżetem")

class Wydatki:
    def __init__(self, przychod, wydatek, data, kategoria):
        self.przychod = przychod
        self.wydatek = wydatek
        self.data = data
        self.kategoria = kategoria

    def wyswietl(self):
       return f"Tutaj jest twój przychód {self.przychod}\nTutaj jest twój wydatek {self.wydatek}\nData: {self.data}\nKategoria: {self.kategoria}"

root = tk.Tk()
root.geometry("500x500")
root.withdraw()

lista_wydatkow = []

zapytanie = input("Czy zacząć wprowadzanie ? y/n ")
while zapytanie.lower() == 'y':
    przychod = float(simpledialog.askstring("Input", "Podaj przychód: "))
    wydatek = float(simpledialog.askstring("Input", "Podaj wydatek: "))
    data = simpledialog.askstring("Input", "Podaj date DD-MM-YYYY: ")
    kategoria = simpledialog.askstring("Input", "Podaj kategorię: ")
    zapytanie = simpledialog.askstring("Input", "Czy chcesz kontynuować wprowadzanie ?  y/n")

    wydatki_uzytk = Wydatki(przychod, wydatek, data, kategoria)
    print(wydatki_uzytk.wyswietl())

    lista_wydatkow.append(wydatki_uzytk)
    if zapytanie.lower() == "n":
        print("Dziękuję, oto twoje statystyki \n-----------------------------")
        for wydatek in lista_wydatkow:
            print(wydatki_uzytk.wyswietl())
            print("-----------------------------")


root.mainloop()
