#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numberOfSwaps = 0
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps += 1
    if not numberOfSwaps:
        break


print("Array is sorted in", numberOfSwaps, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[n-1])
