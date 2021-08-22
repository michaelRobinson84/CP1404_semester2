# Question 1 - Code that asks the user for their name, then opens a file called "name.txt" and writes that name to it

str_name = input("Please enter your name: ")

output_file = open("name.txt", "w")

print(str_name, file=output_file)

output_file.close()

# Question 2 - Code that opens "name.txt" and reads the name then prints "Your name is [name]"

input_file = open("name.txt", "r")

str_name = input_file.readline()
str_name = str_name.strip()

print("Your name is {}.".format(str_name))

input_file.close()

# Question 3

input_file = open("numbers.txt", "r")

str_first_num = input_file.readline()
int_first_num = int(str_first_num)

str_second_num = input_file.readline()
int_second_num = int(str_second_num)

int_result = int_first_num + int_second_num

print("The result is {}".format(int_result))

input_file.close()

# Question 4

int_total = 0

input_file = open("numbers.txt", "r")

for line in input_file:
    temp_number = int(line)
    int_total += temp_number

print("The total of all the numbers in the file is {}".format(int_total))

input_file.close()








