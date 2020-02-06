"""get a folder as a parameter, and go over all object inside it.
it will count all files (only files), and if it is a sub directory , it wont count it. """

import os


def files_count(path):
    counter = 0
    x = os.listdir(path)
    for item in x:
        if os.path.isdir(item):
            continue
        counter += 1

    print(x)
    print('Number of files in current dir is: ' + str(counter))


files_count('c:/Windows')
