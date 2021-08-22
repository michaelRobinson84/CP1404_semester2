def main():

    str_password = get_password()

    print_password(str_password)


def print_password(str_password):
    print((len(str_password) * "*"))


def get_password():
    str_password = input("Please enter a password of minimum length 8 characters: ")
    while len(str_password) < 8:
        print("Password not long enough!")
        str_password = input("Please enter a password of minimum length 8 characters: ")
    return str_password


main()

