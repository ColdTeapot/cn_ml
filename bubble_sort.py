"""
Implement bubble sort for a user inputted list items.
"""

l = [int(x) for x in input().strip().split(" ")]
print("Before sorting: ")
print(l)
n = len(l)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

print("After sorting: ")
print(l)
