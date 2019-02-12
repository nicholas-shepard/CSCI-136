import sys

#List of CLI arguments as ints
nums = list(map(int, sys.argv[1:]))

#Printing min, max, and average
print("Minimum:", min(nums))
print("Maximum:", max(nums))
print("Average:", sum(nums)/len(nums))
