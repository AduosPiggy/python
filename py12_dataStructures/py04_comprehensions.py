vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
a = [x*y for x in vec1 for y in vec2]
print(a) # [8, 6, -18, 16, 12, -36, 24, 18, -54]

a = [x+y for x in vec1 for y in vec2]
print(a) # [6, 5, -7, 8, 7, -5, 10, 9, -3]

a = [vec1[i]*vec2[i] for i in range(len(vec1))]
print(a) # [8, 12, -54]
