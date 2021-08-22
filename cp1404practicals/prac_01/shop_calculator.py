number_of_items = int(input("Enter number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter number of items: "))

total_price = 0

for i in range(number_of_items):
    current_item_price = float(input("Enter item price: "))
    total_price = total_price + current_item_price

if total_price > 100:
    total_price = total_price * 0.9

print("Total price for", number_of_items, "items is $", end='')
print("{:.2f}".format(total_price))
