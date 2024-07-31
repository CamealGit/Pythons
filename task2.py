import task1


while True:
    print("Wybierz która funkcje chcesz zastosować")
    print("1 - dodaj, 2 - odejmij\n3 - pomnoz, 4 - podziel\n5 - potęguj, 6 - zakoncz")
    choice = input("Wybierz opcje: ")
    a = input("Wprowadz pierwsza liczbe: ")
    b = input("Wprowadz druga liczbe: ")

    try:
        choice = int(choice)
    except ValueError:
        print("Nie wpisales liczby VALUEERROR")

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Błąd we wpisywaniu ")
        break
    if choice == 1:
        print(task1.dodaj(a, b))
    elif choice == 2:
        print(task1.odejmij(a, b))
    elif choice == 3:
        print(task1.pomnoz(a, b))
    elif choice == 4:
        print(task1.podziel(a, b))
    elif choice == 5:
        print(task1.poteguj(a, b))
    elif choice == 6:
        break



