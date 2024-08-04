def oblicz(weight, height):
    return weight / pow(height, 2)

while True:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    break

print(f"waga to {weight} kg")
print(f"wzrost to {height} m")
wzor = round(oblicz(weight, height), 2)
print(f"Bmi to {wzor}")

if wzor < 18.5:
    print("Niedowaga")
elif wzor >= 18.5 and wzor < 25:
    print("Waga prawdiłowa")
elif wzor >= 25 and wzor < 30:
    print("Nadwaga")
elif wzor >= 30:
    print("Otyłośc")
