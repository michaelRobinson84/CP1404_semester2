str_password = input("Please enter a password of minimum length 8 characters: ")

while len(str_password) < 8:
    print("Password not long enough!")
    str_password = input("Please enter a password of minimum length 8 characters: ")

print((len(str_password) * "*"))
