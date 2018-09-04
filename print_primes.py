"""
All prime numbers

Given an integer N, print all the prime numbers that lies in between 2 to N (both inclusive).
Print the prime numbers in different lines.

Input Format :

Integer N

Output Format :

Prime number in different lines

Constraints :
1 <= N <= 100

Sample Input :

9

Sample Output :

2
3
5
7

"""

n = int(input())


def print_primes_upto(number):
    if number < 2:
        print('')
    else:
        for i in range(2, number + 1):
            prime = True
            for j in range(2, i):
                if i % j == 0:
                    prime = False
            if prime:
                print(i)


print_primes_upto(n)
