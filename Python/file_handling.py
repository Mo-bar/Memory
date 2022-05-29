# 'a' Append : open file for appending values, create file if not exists
# 'r' [default value] open file for read and show error if the file not exists
# 'w' open file for writing, and create file if not exists.
# 'x' create ceate file, and show error if not exists.

# file = open('path/file.txt', 'r') if you're in working dir you don't need to write the path.

import os
print(os.getcwd()) # get current working dir.
file = open('file.txt','w')
print(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.getcwd())

# --------------------------------
# -- File Handling => Read File --
# --------------------------------

myFile = open("D:\Python\Files\osama.txt", "r")

print(myFile)  # File Data Object
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)

print(myFile.read())
print(myFile.read(5))

print(myFile.readline(5))
print(myFile.readline())
print(myFile.readline())

print(myFile.readlines())
print(myFile.readlines(50))
print(type(myFile.readlines()))

for line in myFile:

  print(line)

  if line.startswith("07"):

    break

# Close The File

myFile.close()

# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

myFile = open("D:\Python\Files\osama.txt", "w")
myFile.write("Hello\n")
myFile.write("Third Line")

myFile = open(r"D:\Python\Files\fun.txt", "w")
myFile.write("Elzero Web School\n" * 1000)

myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

myFile = open("D:\Python\Files\osama.txt", "w")
myFile.writelines(myList)

myFile = open("D:\Python\Files\osama.txt", "a")
myFile.write("Elzero")