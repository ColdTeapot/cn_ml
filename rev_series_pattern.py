"""
Reversing Series Pattern

Print the following pattern for the given number of rows.

Pattern for N = 5

1
3 2
4 5 6
10 9 8 7
11 12 13 14 15

Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :

7

Sample Output :

1
3 2
4 5 6
10 9 8 7
11 12 13 14 15
21 20 19 18 17 16
22 23 24 25 26 27 28

"""

n = int(input())
count, val = 0, 0

for i in range(1, n + 1):
    count += 1
    val += i
    if i % 2 != 0:
        if count == 1:
            j = i
            while j <= val:
                print(j, end=' ')
                j += 1
        else:
            j = val - i + 1
            while j <= val:
                print(j, end=' ')
                j += 1
    else:
        j = val
        while j > val - i:
            print(j, end=' ')
            j -= 1
    print()
