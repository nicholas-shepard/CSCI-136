#This should work for all three - square, rectangle, and ragged arrays

a = [[0, 1, 2, 3, 4], [1, 2], [2, 0, 1]]

b = []

for i in range(len(a)):
    b.append([])
    for j in range(len(a[i])):
        b[i].append(a[i][j])

print(b)
