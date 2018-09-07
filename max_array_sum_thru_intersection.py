"""
Maximise the sum

Given 2 sorted arrays (in increasing order), find a path through the intersections that produces maximum sum and return the maximum sum.
That is, we can switch from one array to another array only at common elements.
If no intersection element is present, we need to take sum of all elements from the array with greater sum.

Input Format :

Line 1 : An integer M i.e. size of first array
 Line 2 : M integers which are elements of first array, separated by spaces
 Line 3 : An integer N i.e. size of second array
 Line 4 : N integers which are elements of second array, separated by spaces

 Output Format :

 Maximum sum value

 Constraints :
1 <= M, N <= 10^6

Sample Input :

6
1 5 10 15 20 25
5
2 4 5 9 15

Sample Output :

81

Sample Output Explanation :
We start from array 2 and take sum till 5 (sum = 11). Then we'll switch to array at element 10 and take till 15. So sum = 36. Now, no elements left in array after 15, so we'll continue in array 1. Hence sum is 81

"""

len1 = int(input())
list1 = [int(x) for x in input().strip().split(" ")]

len2 = int(input())
list2 = [int(x) for x in input().strip().split(" ")]


def find_max_sum_thru_intersection(n1, l1, n2, l2):
    max_sum, sum1, sum2, i, j = 0, 0, 0, 0, 0
    while i < n1 and j < n2:
        if l1[i] < l2[j]:
            sum1 += l1[i]
            i += 1
        elif l2[j] < l1[i]:
            sum2 += l2[j]
            j += 1
        else:
            sum1 += l1[i]
            sum2 += l2[j]
            i += 1
            j += 1
            max_sum += max(sum1, sum2)
            sum1, sum2 = 0, 0
    if i == n1:
        sum2 += sum(l2[j:])
    elif j == n2:
        sum1 += sum(l1[i:])
    if sum1 > sum2:
        max_sum += sum1
    elif sum2 > sum1:
        max_sum += sum2
    return max_sum


print(find_max_sum_thru_intersection(len1, list1, len2, list2))


