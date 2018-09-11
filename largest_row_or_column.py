"""
Largest Row or Column

Given an NxM 2D array, you need to find out which row or column has largest sum (sum of its elements) overall amongst all rows and columns.

Input Format :

Line 1 : 2 integers N and M respectively, separated by space
 Line 2: Single line having N*M elements entered in row wise manner, each separated by space.

 Output Format :

 If row sum is maximum then - "row" row_num max_sum
 If column sum is maximum then - "column" col_num max_sum

 Note : If there are more than one rows/columns with maximum sum consider the row/column that comes first. And if ith row and jth column has same sum (which is largest), consider the ith row as answer.

 Sample Input 1 :

2 2
1 1 1 1

Sample Output 1 :

row 0 2


Sample Input 2 :

3 3
3 6 9 1 4 7 2 8 9

Sample Output 2 :

column 2 25

"""

str = input().strip().split(" ")
n, m = int(str[0]), int(str[1])

l = [int(i) for i in input().strip().split(" ")]
l2D = [[l[m * i + j] for j in range(m)] for i in range(n)]


def find_row_or_col_with_max_sum(list2D):
    row, col, rval, cval, max_sum = False, False, 0, 0, 0
    for i in range(n):
        rsum = 0
        for j in range(m):
            rsum += l2D[i][j]
            if max_sum < rsum:
                max_sum = rsum
                row = True
                rval = i
    for a in range(m):
        csum = 0
        for b in range(n):
            csum += l2D[b][a]
            if max_sum < csum:
                max_sum = csum
                row = False
                col = True
                cval = a
    if row:
        print("row {} {}".format(rval, max_sum))
    else:
        print("column {} {}".format(cval, max_sum))



find_row_or_col_with_max_sum(l2D)


