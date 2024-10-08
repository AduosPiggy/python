
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x')) # 2 1 0

a.insert(2, -1)
a.append(333)
print(a) # [66.25, 333, -1, 333, 1, 1234.5, 333]

print(a.index(333))

a.remove(333)
print(a) # [66.25, -1, 333, 1, 1234.5, 333]

a.reverse()
print(a) # [333, 1234.5, 1, 333, -1, 66.25]

a.sort()
print(a) # [-1, 1, 66.25, 333, 333, 1234.5]


a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a) # [1, 66.25, 333, 333, 1234.5]

[1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a) # [1, 66.25, 1234.5]

[1, 66.25, 1234.5]
del a[:]
print(a) # []
