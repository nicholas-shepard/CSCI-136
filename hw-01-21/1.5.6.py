import sys
import math

nums = []
temp = sys.argv[1:]

for i in range(len(temp)):
    if i == 0:
        nums.append(int(temp[i]))
    else:
        if int(temp[i]) != nums[-1]:
            nums.append(int(temp[i]))

print(nums)
