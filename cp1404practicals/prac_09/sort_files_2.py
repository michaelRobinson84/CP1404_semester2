import shutil
import os


def main():

    os.chdir("FilesToSort")
    lst_file_extensions = []

    for directory_name, subdirectories, filenames in os.walk('.'):

        for filename in filenames:

            str_file_extension = get_file_extension(filename)

            if str_file_extension not in lst_file_extensions:       # If we haven't dealt with this file type before
                lst_file_extensions.append(str_file_extension)
                str_user_input = input("What category would you lie to sort {} files into?".format(str_file_extension))

                try:

                    os.mkdir(str_user_input)

                except FileExistsError:

                    pass

                for filename2 in filenames:                            # For each file in the current directory

                    if get_file_extension(filename2) == str_file_extension: # If the file's extension matches the file
                                                                            # extension we are currently working on

                        shutil.move(filename2, str_user_input)              # Move the file where the user says for it
                                                                            # to go


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
