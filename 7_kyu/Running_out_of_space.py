# Kevin is noticing his space run out!
# Write a function that removes the spaces from the values and returns an array showing the space decreasing.
# For example, running this function on the array ['i', 'have','no','space']
# would produce ['i','ihave','ihaveno','ihavenospace']

def spacey(array):
    str = ""
    res = []
    for i in array:
        str += i
        res.append(str)
    return res

from itertools import accumulate

def spacey1(a):
    return list(accumulate(a))

def spacey2(array):
    return [''.join(array[:i+1]) for i in range(len(array))]

