#!/bin/python
file = open("count.txt", "r")
count = file.read() or "1"
num = int(count)
newnum = num + 1
file.close()
file = open("count.txt", "w")
file.write(str(newnum))
print num

