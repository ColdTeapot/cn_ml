"""
Trailing zeroes in n!

Find and return number of trailing 0s in n factorial without calculating n factorial.

Sample Input

50

Sample Output

12

Input Size Limit

n < 10^11

"""

n = int(input())



"""
Logic for finding trailing zeroes can be found from the URL:
https://www.purplemath.com/modules/factzero.htm

Find the number of trailing zeroes in 101!
Okay, how many multiples of 5 are there in the numbers from 1 to 101? There's 5, 10, 15, 20, 25,...

Oh, heck; let's do this the short way: 100 is the closest multiple of 5 below 101, and 100 ÷ 5 = 20, so there are twenty multiples of 5 between 1 and 101.

But wait: 25 is 5×5, so each multiple of 25 has an extra factor of 5 that I need to account for. How many multiples of 25 are between 1 and 101? Since 100 ÷ 25 = 4, there are four multiples of 25 between 1 and 101.

Adding these, I get 20 + 4 = 24 trailing zeroes in 101!
This reasoning extends to working with larger numbers.

Find the number of trailing zeroes in the expansion of 1000!
Okay, there are 1000 ÷ 5 = 200 multiples of 5 between 1 and 1000. The next power of 5, namely 25, has 1000 ÷ 25 = 40 multiples between 1 and 1000. The next power of 5, namely 125, will also fit in the expansion, and has 1000 ÷ 125 = 8 multiples between 1 and 1000. The next power of 5, namely 625, also fits in the expansion, and has 1000 ÷ 625 = 1.6... um, okay, 625 has 1 multiple between 1 and 1000. (I don't care about the 0.6 "multiples", only the one full multiple, so I truncate my division down to a whole number.)

In total, I have 200 + 40 + 8 + 1 = 249 copies of the factor 5 in the expansion, and thus:

249 trailing zeroes in the expansion of 1000!
The previous example highlights the general method for answering this question, no matter what factorial they give you.

Take the number that you've been given the factorial of.
Divide by 5; if you get a decimal, truncate to a whole number.
Divide by 52 = 25; if you get a decimal, truncate to a whole number.
Divide by 53 = 125; if you get a decimal, truncate to a whole number.
Continue with ever-higher powers of 5, until your division results in a number less than 1. Once the division is less than 1, stop.
Sum all the whole numbers you got in your divisions. This is the number of trailing zeroes.
Here's how the process works:


How many trailing zeroes would be found in 4617!, upon expansion?
I'll apply the procedure from above:

51 :  4617 ÷ 5 = 923.4, so I get 923 factors of 5
52 :  4617 ÷ 25 = 184.68, so I get 184 additional factors of 5
53 :  4617 ÷ 125 = 36.936, so I get 36 additional factors of 5
54 :  4617 ÷ 625 = 7.3872, so I get 7 additional factors of 5
55 :  4617 ÷ 3125 = 1.47744, so I get 1 more factor of 5
56 :  4617 ÷ 15625 = 0.295488, which is less than 1, so I stop here.
Then 4617! has 923 + 184 + 36 + 7 + 1 = 1151 trailing zeroes.

"""


def find_trailing_zeroes_in_factorial(number):
    pow = 1
    count = 0
    while number // (5 ** pow) != 0:
        count += number // (5 ** pow)
        pow += 1
    return count


print(find_trailing_zeroes_in_factorial(n))
