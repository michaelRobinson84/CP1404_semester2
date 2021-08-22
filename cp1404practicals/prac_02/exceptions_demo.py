"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?

A ValueError will occur when the user inputs something other than an integer, e.g. a letter of the alphabet etc.

2. When will a ZeroDivisionError occur?

A ZeroDivisionError will occur when the user inputs a 0 when prompted for the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

Yes - The program could check the value stored in denominator and if zero prompt the user to re-enter it.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")