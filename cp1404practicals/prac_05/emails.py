def main():

    dict_name_to_email = {}

    str_email = input("Email: ")

    while str_email != "":

        lst_email_parts = str_email.split("@")

        str_name = get_name_from_email(lst_email_parts)

        dict_name_to_email[str_name] = str_email

        str_email = input("Email: ")

    print()

    for element in dict_name_to_email:
        print("{} ".format(element), end="")
        print("({})".format(dict_name_to_email[element]))


def get_name_from_email(lst_email_parts):

    if "." in lst_email_parts[0]:
        lst_first_part = lst_email_parts[0].split(".")

        index = 1
        str_first_part = lst_first_part[0]

        for element in lst_first_part:
            if index < len(lst_first_part):
                str_first_part = str_first_part + " " + lst_first_part[index]
                index = index + 1

        str_first_part = str_first_part.title()

        while True:
            str_user_input = input("Is your name {}? (Y/n) ".format(str_first_part))

            if str_user_input == "":
                return str_first_part
            elif str_user_input[0].upper() == "Y":
                return str_first_part
            elif str_user_input[0].upper() == "N":
                return input("Name: ")
            else:
                print("Invalid input!")
    else:

        lst_email_parts[0] = lst_email_parts[0].title()
        while True:
            str_user_input = input("Is your name {}? (Y/n) ".format(lst_email_parts[0]))
            if str_user_input == "":
                return lst_email_parts[0]
            elif str_user_input[0].upper() == "Y":
                return lst_email_parts[0]
            elif str_user_input[0].upper() == "N":
                return input("Name: ")
            else:
                print("Invalid input!")
main()
