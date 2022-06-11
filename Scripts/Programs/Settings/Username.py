import time
import os

while True:
    os.system("py ./Scripts/Programs/Settings/Clear.py")

    print("Username Settings:")
    print("[0] Exit")
    print("[1] Change")

    print("")
    MainInput = str(input("PyShell:\Settings\Username\ "))

    if MainInput == str(0):
        break
    elif MainInput == str(1):
        NameInput = str(input("Name: "))
        open("./Data/Username.data", "w").write(NameInput)
    else:
        print("{" + MainInput + "} is not a command.")
        time.sleep(1)