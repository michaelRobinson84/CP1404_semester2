letters = "abcdefg"
letters_list = list(letters)

print(letters_list)

print(letters_list[:3:2])

print([1, 2, 3, 4, 5][2])

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list_of_lists)
print()
print(max(list_of_lists))
print()

for i in letters_list:
    print(i)
    letters_list.remove(i)
    print(i)

my_list = list("abcdef")

print()

print(my_list[2:])
print(my_list[:2])

my_list[3:] = "1234567890"
print(my_list)

