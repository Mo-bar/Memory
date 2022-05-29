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