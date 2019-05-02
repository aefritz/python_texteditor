import os

def create_file():
    filename = input("What do you want to name your file? ")
    first_line = input("Enter the first line")
    with open(filename, "w+") as file_object:
        file_object.write(first_line)

def read_file():
    print("To be constructed")

print("Hello, World")
response = input("Do you want to write a new file? Y/N ")
if (response == "Y"):
    create_file()
elif (response == "N"):
    print("Here are all the files in this directory")
    files = os.listdir()
    for file in files:
        print(str(files.index(file)) + ") " + file)
    selection = int(input("Choose a file or enter L to change directories"))
