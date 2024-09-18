# Your task is simply to count the total number of lowercase letters in a string.
import re

def lowercase_count(string):
    pattern = r'[a-z]'
    x = re.findall(pattern, string)
    return len(x)