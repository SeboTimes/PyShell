import time

print("")
for Line in open("./LICENSE", "r").readlines():
    print(Line)
    time.sleep(1)
    