"""
Reverse Every Word

Given a string S, reverse each word of a string individually. For eg. if a string is "abc def", reversed string should be "cba fed".

Input Format :

String S

Output Format :

Updated string

Constraints :
1 <= Length of S <= 1000

Sample Input :

Welcome to Coding Ninjas

Sample Output:

emocleW ot gnidoC sajniN
"""

s = input("Enter a string: ")

temp = ""
new_s = ""

for c in s:
    if c != " ":
        temp += c
    else:
        new_s += " " + temp[::-1]
        temp = ""

new_s += " " + temp[::-1]
s = new_s.strip()
print(s)
