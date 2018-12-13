import os

os.chdir("E:\\python")
string =""

fname = open("input.txt", 'r')
for line in fname:
    words = len(line.split(" "))
    chars = len(line)
    string += "Number of Words in line = %s\nNumber of Characters in line = %s\n" % (words, chars)

f = open("output.txt", "w+")
f.write(string)
f.close()
