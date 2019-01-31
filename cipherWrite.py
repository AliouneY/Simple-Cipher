# When the user creates a new text file, they type what they need to type, and when they press a command of some sort it "escapes" (perhaps printing a series of spaces; preferrably clearing the entire command line screen and even deploying a decoy program) and ciphers the text file. When the user opens an existing file, it should be readable, but from the outside it should always appear encrypted 

import os

def printMenu():
    print("")
    print("")
    print("===================================================================")
    print("= ~(*0*)~  =========  Welcome to Cipher Write  =========  ~(*0*)~ =")
    print("===================================================================")
    print("=                                                                 =")
    print("=              'h' for help                                       =")
    print("=                                                                 =")
    print("=              'open' file_name to open/create a text file        =")
    print("=                                                                 =")
    print("=              'ls' view list of entries                          =")
    print("=                                                                 =")
    print("=              'q' to quit                                        =")
    print("=                                                                 =")
    print("=              'menu' to see this message again                   =")
    print("=                                                                 =")
    print("===================================================================")
    print("= ~(*0*)~  =============================================  ~(*0*)~ =")
    print("===================================================================")

def cipherFile(input):
    targetFile = open(input, 'r+')
    Arr = []

    for line in targetFile:
        Arr.append(list(line))

    for lst in Arr:
        for i in range(0, len(lst)):
            lst[i] = chr(ord(lst[i]) + 1)

    i = 0
    for lst in Arr:
        lst = "".join(lst)
        Arr[i] = lst
        i = i+1

    targetFile = open(input, "w")
    targetFile.write(Arr[0])
    targetFile = open(input, "a")

    for i in range(1, len(Arr)):
        targetFile.write(Arr[i])

def decipherFile(input):
     targetFile = open(input, 'r+')
     Arr = []

     for line in targetFile:
         Arr.append(list(line))

     for lst in Arr:
         for i in range(0, len(lst)):
             lst[i] = chr(ord(lst[i]) - 1)

     i = 0
     for lst in Arr:
         lst = "".join(lst)
         Arr[i] = lst
         i = i+1

     targetFile = open(input, "w")
     targetFile.write(Arr[0])
     targetFile = open(input, "a")

     for i in range(1, len(Arr)):
         targetFile.write(Arr[i])



def openTextFile(input):
    if(len(input) > 4 and input[4] == ' '):
        fileName = input[5:]
        if not fileName[-4:] == '.txt':
            fileName = fileName + ".txt"
        if os.path.exists(fileName):
            decipherFile(fileName)
            os.system("vim " + fileName)
            cipherFile(fileName)
            os.system("clear")
            os.system("vim mechinism.py")

        else:
            os.system("vim " + fileName)
            if os.path.exists(fileName):
                cipherFile(fileName)
                os.system("vim mechinism.py")

    else:
        print("Command not recognized...")


def printHelp():
    print("This is a cipher. It lets you write into text files and encrypt ")
    print("them so that noone can read them unless they use this program ")
    print("(or guess the encryption key...). ")


def cipherWrite():
    os.chdir("entries/")
    printMenu()

    userSelection = None

    while (userSelection != "q"):
        userSelection = input("~(*0*)~")

        if (userSelection == "h"):
            printHelp()
        
        elif(userSelection == "ls"):
            os.system("ls")

        elif(userSelection[:4] == "open"):
            openTextFile(userSelection)

        elif(userSelection == "menu"):
            printMenu()

        elif(userSelection == "q"):
            print("Quiting...")
            os.chdir("..")

        else:
            print("command not recognized...")

cipherWrite()
