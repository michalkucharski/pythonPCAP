import re

#script to find the longest word in the string
def get_longest_word(input_string):

    #as a patter put the symbols with are used to split the words
    words = re.split(r'[,,\s, .]+',input_string)

    return max(words, key=len)