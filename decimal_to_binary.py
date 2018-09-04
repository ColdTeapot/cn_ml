"""
Decimal to Binary

Given a decimal number (integer N), convert it into binary and print.
The binary number should be in the form of an integer.
Note : The given input number could be large, so the corresponding binary number can exceed the integer range. So take the answer as long.

Input format :

Integer N

Output format :

Corresponding Binary number (long)

Sample Input 1 :

12

Sample Output 1 :

1100

Sample Input 2 :

7

Sample Output 2 :

111

"""

n = int(input())


def get_quotient_on_division_by_2(decimal):
    return decimal // 2


def get_remainder_on_division_by_2(decimal):
    return decimal % 2


def convert_decimal_to_binary(decimal):
    dividend = decimal
    str_remainders = ""

    while dividend != 0:
        remainder = str(get_remainder_on_division_by_2(dividend))
        str_remainders += remainder
        quotient = get_quotient_on_division_by_2(dividend)
        dividend = quotient
    return int(str_remainders[::-1])


print(convert_decimal_to_binary(n))

