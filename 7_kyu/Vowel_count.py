# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    num_v = 0
    for char in sentence:
        if char in 'aeiouAEIOU':
            num_v += 1
    return num_v