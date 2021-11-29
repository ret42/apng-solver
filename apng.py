#!/usr/bin/python3
pw=""
for i in range(1,14): #if you have 94 frame then put 94 instead of 14 (btw add + 1)
    if i < 10:
        i = "0" + str(i)
    f = open("apngframe" + str(i) + ".txt")
    l = f.read()
    pw += chr(int(l.split("/")[0][6:]))
print(pw)
