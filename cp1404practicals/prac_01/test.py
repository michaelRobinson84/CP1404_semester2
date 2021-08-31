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

print("*************************************************************************")
print()
my_list = ['a', [1, 2, 3, 4, 5, 6, 7, 8, 9], 'z']
print(my_list[1])
print(my_list[1][2])
print("The length of the outer list is ", end='')
print(len(my_list))
print("The length of the inner list is ", end='')
print(len(my_list[1]))
print()
my_str = "This is a test"
string_elements = my_str.split()
print(string_elements)
reversed_elements = []
for element in string_elements:
    reversed_elements.append(element[::-1])

print(reversed_elements)
new_str = ' '.join(reversed_elements)
print(new_str)
print()
numbers = [10, 20, 30]
things = numbers
numbers.append(40)
print(numbers)
print(things)
print()

scores = []
score = int(input("Score: "))
while score >= 0:
    scores.append(score)
    score = int(input("Score: "))
print("Your highest score is", max(scores))
print()
tup = 2, 3
print(type(tup))
print(tup)
print()

my_tup = (1)
my_tup2 = (1,)
print(type(my_tup))
print(type(my_tup2))
print()

date_input = input("Enter DOB (d/m/y)")
parts = date_input.split("/")
my_dob = (int(parts[0]), int(parts[1]), int(parts[2]))
print(my_dob)
print(type(parts))
print(type(my_dob))