from prac_06.guitar import Guitar

print("My guitars!")

guitars = []

name = input("Name: ")

while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    current_guitar = Guitar(name, year, cost)
    guitars.append(current_guitar)
    name = input("Name: ")

print("These are my guitars:")

i = 0

for guitar in guitars:
    print("Guitar {}: {} ({}), worth ${}".format(i + 1, guitar.name, guitar.year, guitar.cost),end="")
    if guitar.is_vintage():
        print(" (vintage)")
    else:
        print("")

    i +=1