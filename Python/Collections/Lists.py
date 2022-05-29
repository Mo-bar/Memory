# -----------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed between  Square Brackets
# [2] List Are Ordered
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types

lst = ["One", "Two", "One", 1, 100.5, True]
print('lst[0] ='+lst[0])
print('lst[-1] ='+str(lst[-1]))
print('lst[-3] ='+str(lst[-3]))
print(lst[1:4]) #['Two', 'One', 1]
print(lst[:4]) # ['One', 'Two', 'One', 1]
print(lst[4:]) # [100.5, True]

print('='*50)
#___Methods.
friends = ['ali','mouad','simon']
friends.append('yasmine') # add
print(friends)
nbr = [23,23,44]
friends.append(nbr) # add list , friends list became multi demnsions
print(friends[-1][2])
friends.extend(nbr)  # friends += nbr
print(friends)
print('_'*50)
friends.sort(reverse=True)
friends.remove('mouad')
nbr.reverse()
print(nbr)


# clear()

a = [1, 2, 3, 4]
a.clear()
print(a)

# copy()

b = [1, 2, 3, 4]
c = b.copy()

print(b)  # Main List
print(c)  # Copied List

b.append(5)

print(b)  # Main List
print(c)  # Copied List

# count()

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

# index()

e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))

# insert()

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")

print(f)

# pop()

g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))