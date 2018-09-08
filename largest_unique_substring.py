"""
Largest Unique Substring

Given a string S, find the largest substring with no repetition i.e. largest substring which contain all unique characters.

Input Format :

String S

Output Format :

Largest unique substring

Constraints :
1 <= Length os String S <= 10^3

Sample Input:

abcdabceb

Sample Output:

dabce

"""

input_str = input()


def find_largest_unique_substring(str):
    result = list()
    best = list()
    if len(str) == 1:
        return 1
    for num,i in enumerate(str):
        if i in result:
            index = result.index(i)
            result = result[index+1:]

        result.append(i)
        if len(best) < len(result):
            best = list(result)
    largest_unique_substr = ""
    for i in range(len(best)):
        largest_unique_substr += best[i]
    return largest_unique_substr


print(find_largest_unique_substring(input_str))
