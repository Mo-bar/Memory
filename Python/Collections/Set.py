# -- Set --
# ---------
# {1} Set Items Are Enclosed between Curly Braces
# {2} Set Items Are Not Ordered And Not Indexed
# {3} Set Indexing and Slicing Cant Be Done
# {4} Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# {5} Set Items Is Unique

mySetOne = {"Osama", "Ahmed", 100}
print(mySetOne)
# print(mySetOne[0]) error
mySetThree = {"Osama", 100, 100.5, True, (1, 2, 3)}

print(mySetThree)

# -- Set Methods --
# -----------------

# clear()

a = {1, 2, 3}
a.clear()
print(a)

# union()

b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Cool"}

print(b | c)
print(b.union(c, x))

# add()

d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d)

# copy()

e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(6)

print(e)
print(f)

# remove()

g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7)
print(g)

# discard()

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
print(h)

# pop()

i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())

# update()

j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(['Html', "Css"])
j.update(k)

print(j)

# -----------------
# -- Set Methods --
# -----------------

# issuperset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b))  # True
print(a.issuperset(c))  # False

print("=" * 50)

# issubset()

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e))  # False
print(d.issubset(f))  # True

print("=" * 50)

# isdisjoint()

g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h))  # False
print(g.isdisjoint(i))  # True