"""
Even Fibonacci Numbers

Given a number N find the sum of all the even valued terms in the fibonacci sequence less than or equal to N. Try generating only even fibonacci numbers instead of iterating over all Fibonacci numbers.

Input Format

Line 1 : An integer N

Output Format

Total Sum

Input Constraints

1 <= N <= 10^6

Sample Input 1:

8

Sample Output 1 :

10

Sample Input 2:

400

Sample Output 2:

188
"""

n = int(input())


def sum_of_even_fibo(num):
    a, b, sum = 0, 1, 0
    while b <= num:
        if b % 2 == 0:
            sum += b
        a, b = b, a + b
    return sum

print(sum_of_even_fibo(n))
