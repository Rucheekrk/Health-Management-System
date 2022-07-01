# Health Management
import os, os.path

# Function to retrieve diet and exercise file from the respective person's folders.
def retrieve(file):
    print("Enter 1 to select diet file.\nEnter 2 to select exercise file.")
    sel = int(input())
    if sel == 1:
        with open(file + "_diet.txt ") as f:
            print(f.read())
    elif sel == 2:
        with open(file + "_exer.txt ") as f:
            print(f.read())


def log(file):
    print("Enter 1 to select diet file.\nEnter 2 to select exercise file.")
    selec = int(input())
    if selec == 1:
        with open(file + "_diet.txt", "a") as f:
            type = input("PLease start typing to add: ")
            f.write(str([str(getdate())])+"  "+type+"\n")
            print("Successfully Added.\n")
    elif selec == 2:
        with open(file + "_exer.txt", "a") as f:
            type = input("PLease start typing to add: ")
            f.write(str([str(getdate())]) + "  " + type + "\n")
            print("Successfully Added.\n")


def getdate():
    import datetime
    return datetime.datetime.now()


def addPerson(name):
    # with open(name+".txt","w") as f:
    directory = name
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir,directory)
    os.mkdir(path)
    file = os.path.join(path,name)
    print("Welcome " + name)
    with open(file+"_exer.txt","w") as f1, open(file+"_diet.txt","w") as f2:
        print("You folder is ready.")
    print("Please enter 1 to log a file.\nEnter 0 to Exit.")
    inp = int(input())
    # if inp == 1:
    #     retrieve(file)
    if inp == 1:
        log(file)
    elif inp == 0:
        print("CLosing...\nThank you.")

print("Welcome to Health Management System")

while True:
    name = input("Enter the name:")
    if name == '':
        print("You entered an invalid name.")
        break;
    # from os.path import exists
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, name)
    isdir = os.path.isdir(path)
    if not isdir:
        addPerson(name)
    else:
        file = os.path.join(path, name)
        print("Welcome " + name)
        print("Please enter 1 to retrieve or 2 to log a file.\nEnter 0 to Exit.")
        inp = int(input())
        if inp == 1:
            retrieve(file)
            continue
        elif inp == 2:
            log(file)
            continue
        elif inp == 0:
            print("CLosing...\nThank you.")
        break
