# Filter the number
# Oh, no! The number has been mixed up with the text. Your goal is to retrieve the number from the text,
# can you return the number back to its original state?
#
# Task
# Your task is to return a number from a string.
#
# Details
# You will be given a string of numbers and letters mixed up,
# you have to return all the numbers in that string in the order they occur.
#
import re

def filter_string(st):
    pattern = r'\D'
    x = re.sub(pattern, "", st)
    return int(x)

def filter_string(string):
    return int(''.join(filter(str.isdigit, string)))

def filter_string(string):
    return int(''.join(a for a in string if a.isdigit()))