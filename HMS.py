# Health Management
import os, os.path
import pickle

# Function to RETRIEVE diet and exercise file from the respective person's folders.
def retrieve(file):
    print("Enter 1 to select diet file.\nEnter 2 to select exercise file.")
    sel = int(input())
    if sel == 1:
        with open(file + "_diet.txt") as f:
            print(f.read())
            f.close()
    elif sel == 2:
        with open(file + "_exer.txt") as f:
            print(f.read())
            f.close()

# Function to LOG diet and exercise file from the respective person's folders.
def log(file):
    print("Enter 1 to select diet file.\nEnter 2 to select exercise file.")
    selec = int(input())
    if selec == 1:
        with open(file + "_diet.txt", "a") as f:
            type = input("PLease start typing to add: ")
            f.write(str([str(getdate())])+"  "+type+"\n")
            print("Successfully Added.\n")
            f.close()
    elif selec == 2:
        with open(file + "_exer.txt", "a") as f:
            type = input("PLease start typing to add: ")
            f.write(str([str(getdate())]) + "  " + type + "\n")
            print("Successfully Added.\n")
            f.close()

# Function to get data and time
def getdate():
    import datetime
    return datetime.datetime.now()


# Creating the folder to save passwords

# Function to verify the password
def passwd(name):
    pwd = input("Enter password:")
    with open('password_data.pkl', 'rb') as fp:
        pkl_data = pickle.load(fp)
        fp.close()
        print(pkl_data)
    if pwd == pkl_data[name]:
        print("Access Granted")
        return 1
    else: 
        print("Access Denied")
        return 0
    

# Function to add a new user
def addPerson(name, pwdDict):
    #creating directory of the user
    # with open(name+".txt","w") as f:
    directory = name
    parent_dir = os.getcwd()
    print(parent_dir)
    path = os.path.join(parent_dir,directory)
    os.mkdir(path)
    print(path)
    file = os.path.join(path,name)

    #creating and saving password
    while True:
        pwd = input("Create password:")
        pwd1 = input("Re-enter password:")
        if pwd == pwd1:
            user1 = (pwd)
            while True:
                try:
                    with open('password_data.pkl', 'rb') as fp:
                        pwdDict = pickle.load(fp)
                        fp.close()
                    print(pwdDict)
                    pwdDict[name] = user1
                    with open('password_data.pkl', 'wb') as fp:
                        pickle.dump(pwdDict, fp)
                        fp.close()
                    print(pwdDict)
                    break
                except:
                    print(pwdDict)
                    pwdDict[name] = user1
                    print(pwdDict)
                    with open('password_data.pkl', 'wb') as fp:
                        pickle.dump(pwdDict, fp)
                        fp.close()
                    break
            print("Account successfully created")
            break
        else: print("Password doesn't match")


    #creating folders of the user
    print("Welcome " + name)
    with open(file+"_exer.txt","a") as f1, open(file+"_diet.txt","a") as f2:
        print("You folder is ready.")
    f1.close(), f2.close()
    print("Please enter 1 to log a file.\nEnter 0 to Exit.")
    inp = int(input())
    if inp == 1:
        log(file)
    elif inp == 0:
        print("CLosing...\nThank you.")


#Start of the program
print("Welcome to Health Management System")

# Creating password folder (creates a new Password folder for only once in a new device.)
'''password = "Password"
parent_dir = os.getcwd()
path = os.path.join(parent_dir, password)
isdir = os.path.isdir(path)
if not isdir:
    os.mkdir(path)
'''

# Creating an empty dictionary to store passwords
pwdDict = dict()
if not os.path.isfile('password_data.pkl'):
    with open('password_data.pkl', 'wb') as fp:
        fp.close()

while True:
    name = input("Enter the name:")
    if name == '':
        print("You entered an invalid name.")
        break
    # from os.path import exists
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, name)
    isdir = os.path.isdir(path)
    if not isdir:
        addPerson(name, pwdDict)
    else:
        file = os.path.join(path, name)
        print("Welcome " + name)
        if passwd(name) == 1 : pass
        elif passwd(name) == 0 : continue
        print("Please enter 1 to log or 2 to retrieve a file.\nEnter 0 to Exit.")
        inp = int(input())
        if inp == 1:
            log(file)
            continue
        elif inp == 2:
            retrieve(file)
            continue
        elif inp == 0:
            print("CLosing...\nThank you.")
        break
