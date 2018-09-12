"""
Spiral Print

Given an N*M 2D array, print it in spiral form. That is, first you need to print the 1st row, then last column, then last row and then first column and so on.

Print every element only once.

Input format :

Line 1 : N and M, No. of rows & No. of columns (separated by space) followed by N*M  elements in row wise fashion.

Sample Input :

4 4 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

Sample Output :

1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

"""

str = input().strip().split(" ")
n, m = int(str[0]), int(str[1])

l = [int(x) for x in str][2:]

l2D = [[l[m * i + j] for j in range(m)] for i in range(n)]


def print_spiral(num_rows, num_cols, list2D):
    row, col = 0, 0
    while row < num_rows and col < num_cols:
        for i in range(col, num_cols):
            print(list2D[row][i], end=" ")
        row += 1
        for i in range(row, num_rows):
            print(list2D[i][num_cols - 1], end=" ")
        num_cols -= 1
        if row < n:
            for i in range(num_cols - 1, col - 1, -1):
                print(list2D[num_rows - 1][i], end=" ")
            num_rows -= 1
        if col < m:
            for i in range(num_rows - 1, row - 1, -1):
                print(list2D[i][col], end=" ")
            col += 1


print_spiral(n, m, l2D)

