from genericpath import exists
import random
import tqdm
import time
import os

FirstStartBarTime = random.randint(25, 100)
StartBarTime = random.randint(10, 25)

if open("Data/FirstStart.data", "r").read() == "True":
    StartBarTime = FirstStartBarTime
    open("Data/FirstStart.data", "w").write("False")
for StartBar in tqdm.tqdm(range(StartBarTime)):
        time.sleep(0.1)
if open("Data/Username.data", "r").read() == " ":
    print("")
    NewName = input("Name: ")
    open("Data/Username.data", "w").write(NewName)
        
print("")
print("Sebo-Dos Version: 1.8")
print("")
print("Hello " + str(open("Data/Username.data", "r").read()) + "!")

def DosMain():
    Icommand = ["close", "return", "help"]

    print("")
    MainInput = str(input("Sebo-Dos:\ "))
    if MainInput == Icommand[0]:
        open("Data/Closed.data", "w").write("True")
    elif MainInput == Icommand[1]:
        open("Data/Closed.data", "w").write("True")
        open("Data/Returned.data", "w").write("True")
    elif MainInput == Icommand[2]:
        print("Commands:")
        for Icommands in Icommand:
            print(Icommands)
        for commands in os.listdir("Scripts/Commands/"):
            print(commands[:-3])
        print("")
        print("Programs:")
        for commands in os.listdir("Scripts/Programs/"):
            print(commands[:-3])
        DosMain()
    elif exists("Scripts/Commands/" + MainInput + ".py") == True:
        os.system("py Scripts/Commands/" + MainInput + ".py")
        DosMain()
    elif exists("Scripts/Programs/" + MainInput + ".py") == True:
        os.system("py Scripts/Programs/" + MainInput + ".py")
        DosMain()
    else:
        print("{" + MainInput + "} is not a command, try {help}.")
        DosMain()

DosMain()