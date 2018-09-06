"""
Reverse string Word Wise

Reverse the given string word wise. That is, the last word in given string should come at 1st place, last second word at 2nd place and so on. Individual words should remain as it is.

Sample Input:

Welcome to Coding Ninjas

Sample Output:

Ninjas Coding to Welcome

"""

str = input()

def rev_string_word_wise(str_input):
    rev_str = ""
    aux_list = str_input.split(" ")
    aux_list = aux_list[::-1]
    for word in aux_list:
        rev_str += word + " "
    print(rev_str.strip())

rev_string_word_wise(str)
