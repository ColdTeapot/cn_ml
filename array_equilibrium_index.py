"""
Array Equilibrium Index

Find and return the equilibrium index of an array. Equilibrium index of an array is an index i such that the sum of elements at indices less than i is equal to the sum of elements at indices greater than i.
Element at index i is not included in either part.
If more than one equilibrium index is present, you need to return the first one. And return -1 if no equilibrium index is present.
Input format :

Line 1 : Size of input array

Line 2 : Array elements (separated by space)

Sample Input:

7
-7 1 5 2 -4 3 0

Output:

3

"""

n = int(input())
l = [int(x) for x in input().strip().split(" ")]

def find_equilibrium(list):
    list_len = len(list)
    total_sum = sum(list)
    r_sum = 0
    equilibrium_index = 0
    has_equilibrium = False
    for i in range(list_len - 1, -1, -1):
        if r_sum == total_sum - (list[i] + r_sum):
            has_equilibrium = True
            equilibrium_index = i
        r_sum += list[i]
    if has_equilibrium:
        return equilibrium_index
    return -1


print(find_equilibrium(l))
