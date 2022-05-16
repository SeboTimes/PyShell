from Scripts import Install, SeboDos
import time
import os

if open("./Data/NewInstall.data", "r").read() == "True":
    open("./Data/NewInstall.data", "w").write("False")
    os.system("py Scripts/NewLaunch.py")

command = ["close", "help", "reset", "install", "sebo-dos"]
Start = True

def DataError():
        print("")
        print(open("./Errors/Data.error", "r").read())
        time.sleep(10)

while True:
    if Start == True:
        Start = False
    elif Start == False:
        print("")
    else:
        print("")
        print(open("./Errors/Unknown.error", "r").read())
        time.sleep(10)
        break
    MainInput = str(input("Launcher: "))
    if MainInput == command[0]:
        break
    if MainInput == command[1]:
        print("Commands:")
        for commands in command:
            print(commands)
    elif MainInput == command[2]:
        open("./Data/Installed.data", "w").write("False")
        open("./Data/FirstStart.data", "w").write("True")
        open("./Data/Username.data", "w").write(" ")
    elif MainInput == command[3]:
        Install.Install()
        open("./Data/Installed.data", "w").write("True")
    elif MainInput == command[4]:
        print("")
        if open("./Data/Installed.data", "r").read() == "True":
            SeboDos.Main()
            if open("./Data/Closed.data", "r").read() == "True":
                if open("./Data/Returned.data", "r").read() == "True":
                    open("./Data/Closed.data", "w").write("False")
                    open("./Data/Returned.data", "w").write("False")
                elif open("./Data/Returned.data", "r").read() == "False":
                    open("./Data/Closed.data", "w").write("False")
                    break
                else:
                    DataError()
                    break
            elif open("./Data/Closed.data", "r").read() == "False":
                print("")
                print(open("./Errors/Crash.error", "r").read())
            else:
                DataError()
                break
        elif open("./Data/Installed.data", "r").read() == "False":
           print(open("./Errors/NotInstalled.error", "r").read())
        else:
            DataError()
            break
    else:
        print("{" + MainInput + "} is not a command!")
