numeracja = 0
while True:
    f = open('readme.txt', 'a')
    tekst = input("Wpisz zadanie: (0 żeby zakończyć wprowadzanie)\nZadanie: ")
    if tekst == '0':
        break
    status = int(input("Zrobione czy nie(1/0)"))
    if status in [0,1]:
        f.write(str(numeracja) + '. ' + tekst + ';' + str(status) + "\n")
        f = open('readme.txt', 'r')
        print(f.read())
        f.close()
        numeracja = numeracja + 1
    else:
        break

