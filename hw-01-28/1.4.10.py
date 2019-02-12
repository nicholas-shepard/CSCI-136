a = [[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1]]

b = []

for i in range(len(a[0])):
    b.append([])

for i in range(len(a)):
    for j in range(len(a[i])):
        b[j].append(a[i][j])

print(a)
print(b)
