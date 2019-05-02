import os

def create_file():
    filename = input("What do you want to name your file? ")
    first_line = input("Enter the first line")
    with open(filename, "w+") as file_object:
        file_object.write(first_line)
    main()

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
    editloop = True
    print("Press enter to write a new line or Q to quit\n")
    while editloop:
        newline = input("")
        if (newline == 'Q'):
            break
        else:
            newline = '\n' + newline
            with open(filename, "a") as file_object:
                file_object.write(newline)
    main()

def switch_parent():
    os.chdir("..")
    main()

def main():
    print("\nHere are all the files in this directory\n")
    files = os.listdir()
    for file in files:
        print(str(files.index(file)) + ") " + file)
    print("\n")
    selection = input("Enter file no. to select file\nEnter L to change directories\nEnter N to create a new file\nEnter Q to quit\n")
    print(selection)
    int_bool = False
    try:
        fileno = int(selection)
    except:
        int_bool = False
    else:
        int_bool = True
    if (selection == 'L'):
        print('Chose L')
    elif (selection == 'N'):
        create_file()
    elif (selection == 'Q'):
        print('Goodbye')
    elif (int_bool):
        if (int(selection) >= 0 and int(selection) <= len(files)):
            read_file(files[int(selection)])
        else:
            print('Invalid input. Select a valid file')
            main()
    else:
        print('Invalid input')
        main()
main()
