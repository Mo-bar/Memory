# ---------------------------------
# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists

string = 'Hello Python.'
print("string[0] = "+string[0])
print("string[-1] = "+string[-1]) # the last index.
print("string[-3] = "+string[-3]) # the third index start from the end.

# Access multi sequence  item.
# [start:end] end not enclude.
print("string[1:4] = "+string[1:4])
print("string[:4] = "+string[:4]) # printing from index 0 to 3
print("string[4:] = "+string[4:]) # printing from index 4 to the end.
print("string[:] = "+string[:]) # full data.

