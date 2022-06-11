import time
import os

while True:
    os.system("py ./Scripts/Programs/Settings/Clear.py")

    print("Settings:")
    print("[0] Exit")
    print("[1] Username")
    #print("[2] Password")
    
    print("")
    MainInput = str(input("PyShell:\Settings\ "))

    if MainInput == str(0):
        break
    elif MainInput == str(1):
        os.system("py ./Scripts/Programs/Settings/Username.py")
    elif MainInput == str(2):
        os.system("py ./Scripts/Programs/Settings/Password.py")
    else:
        print("{" + MainInput + "} is not a command.")
        time.sleep(1)
