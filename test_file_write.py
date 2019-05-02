import os

def create_file():
    filename = input("What do you want to name your file? ")
    first_line = input("Enter the first line")
    with open(filename, "w+") as file_object:
        file_object.write(first_line)

def read_file(filename):
    with open(filename) as file_object:
        lines = file_object.readlines()
        for line in lines:
            print(line)
    useraction = input("Would you like to modify this file? Y/N ")
    if (useraction == 'Y'):
        edit_file(filename)
    else:
        main()

def edit_file(filename):
    print("To be constructed")


def main():
    print("Here are all the files in this directory")
    files = os.listdir()
    for file in files:
        print(str(files.index(file)) + ") " + file)
    selection = int(input("Select a file\nEnter L to change directories\nEnter N to create a new file\nEnter Q to quit "))

main()
