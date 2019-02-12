a = [[True, False, False], [False, False, True], [True, True, True]]

for i in range(len(a)):
    for j in range(len(a[i])):
        if (a[i][j] == True):
            print("*", end = "")
        else:
            print(" ", end = "")
    print()
