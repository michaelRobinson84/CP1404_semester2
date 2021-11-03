import shutil
import os


def main():

    lst_file_types = []

    os.chdir("FilesToSort")

    for directory_name, subdirectories, filenames in os.walk('.'):

        for filename in filenames:

            file_extension = get_file_extension(filename)

            if file_extension not in lst_file_types:

                lst_file_types.append(file_extension)
                os.mkdir(file_extension)
                shutil.move(filename, file_extension)
            else:
                shutil.move(filename, file_extension)


def get_file_extension(filename):

    index = 0

    for char in filename:
        if char != ".":
            index += 1
        else:
            index += 1
            file_extension = filename[index:]
            return file_extension


main()
