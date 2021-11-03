"""
CP1404/CP5632 Practical
Intermediate exercises
"""
import shutil
import os


def main():

    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:

            old_address = os.path.join(directory_name, filename)

            new_name = get_fixed_filename(filename)

            new_address = os.path.join(directory_name, new_name)

            os.rename(old_address, new_address)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""

    new_name = ""
    new_name_2 = ""
    new_name_3 = ""

    filename = filename.replace(" ", "_")

    index = 0

    for char in filename:
        if char.islower():                          # if the character is lowercase
            try:
                if filename[index + 1].isupper():   # if the next character is uppercase
                    new_name += char
                    new_name += "_"
                else:
                    new_name += char
            except IndexError:                      # we are at the last character in filename
                new_name += char
        else:
            new_name += char

        index += 1

    new_name = new_name.replace(".TXT", ".txt")

    index = 0

    for char in new_name:

        if char.islower() and new_name[index - 1] == "_":   # If a lowercase letter follows an underscore
            new_name_2 += char.upper()                      # Change letter to uppercase
        else:
            new_name_2 += char

        index += 1

    index = 0

    for char in new_name_2:
        if char.islower() and index == 0:                   # If the first letter in the string is lowercase
            new_name_3 += char.upper()                      # Change letter to uppercase
        else:
            new_name_3 += char

        index += 1

    return new_name_3


main()
