import time

print("")
FileInput = str(input("File-Path: "))
print("")
for Line in open(FileInput, "r").readlines():
    print(Line)
    time.sleep(1)