def oblicz(weight, height):
    return weight / pow(height, 2)

print("Witaj w kalkulatorze zdrowia")
while True:
    try:
        wiek = int(input("Wpisz swój wiek: "))
        weight = float(input("Wpisz swoją wagę w kg: (np. 70.4): "))
        height = float(input("Wpisz swój wzrost w meterach: (np. 1.68): "))

        if height < 0.5 or height > 3.0:
            print("Wartości nie mogą być mniejsze od 0")
            continue
        if 0.5 < height > 3.0:
            print("Wpisano zły wzrost, spróbuj ponownie")
            continue
        if wiek < 0 or wiek > 100:
            print("Wpisano zły wiek, spróbuj ponownie")
            continue

        break
    except ValueError:
        print("Wpisano złą wartość")

lista = ["Niedowaga", "Waga prawidłowa", "Nadwaga", "Otyłość"]
def wynik(bmi):
    if bmi < 18.5:
        return lista[0]
    elif bmi >= 18.5 and bmi < 25:
        return lista[1]
    elif bmi >= 25 and bmi < 30:
        return lista[2]
    elif bmi >= 30:
        return lista[3]


print(f"Twoja waga to {weight} kg")
print(f"Twój wzrost to {height} m")
wzor_bmi = round(oblicz(weight, height), 2)

while True:
    try:
        plec = input("Podaj swoją płeć (K lub M)")
        if plec.lower() == "m":
            wzor_tkanka_m = (1.20 * wzor_bmi) + (0.23 * wiek) - 16.2
            print(f"Twoja szacowana tkanka tłuszczowa na podstawie danych to {wzor_tkanka_m:.1f} %")
            print(f"Twoje BMI to {wzor_bmi}, {wynik(wzor_bmi)}")
            break
        elif plec.lower() == "k":
            wzor_tkanka_k = (1.20 * wzor_bmi) + (0.23 * wiek) - 5.4
            print(f"Twoja szacowana tkanka tłuszczowa na podstawie danych to {wzor_tkanka_k:.1f} %")
            print(f"Twoje BMI to {wzor_bmi}, {wynik(wzor_bmi)}")
            break
        else:
            print("Wprowadzono złą wartość")
            continue
    except ValueError:
        print("Wprowadzono złą wartość")

