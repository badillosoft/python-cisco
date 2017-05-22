# _*_ coding: utf-8 _*_

# LISTAS

a = []

a.append(1)
a.append(3)
a.append(5)
a.append(7)
#...

print a

a.pop() # [1, 3, 5] 😉

a.pop(0) # [3, 5]

a.insert(1, 6) # [3, 6, 5]

a.remove(6) # [3, 5]

print a
