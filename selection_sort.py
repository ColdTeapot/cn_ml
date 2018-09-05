"""
Selection Sort

Given a random integer array. Sort this array using selection sort.
Change in the input array itself. You don't need to return or print elements.
Input format :

Line 1 : Array Size

Line 2 : Array elements (separated by space)

Sample Input 1:

7
2 13 4 1 3 6 28

Sample Output 1:

1 2 3 4 6 13 28

Sample Input 2:

5
9 3 6 2 0

Sample Output 2:

0 2 3 6 9

"""

n = int(input())
l = [int(x) for x in input().strip().split(" ")]

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if l[j] < l[min_index]:
            min_index = j
    l[i], l[min_index] = l[min_index], l[i]

output = ""
for x in l:
  output += str(x) + " "
output = output.strip()
print(output)
