# Write a function that takes as parameters an array (arr) and 2 integers (x and y).
# The function should return the mean between the mean of the the first x elements of the array
# and the mean of the last y elements of the array.
#
# The mean should be computed if both x and y have values higher than 1
# but less or equal to the array's length. Otherwise the function should return -1.
#
# Examples
# [1, 3, 2, 4], 2, 3 => should return 2.5
# because: the mean of the the first 2 elements of the array is (1+3)/2=2
# and the mean of the last 3 elements of the array is (4+2+3)/3=3 so the mean of those 2 means is (2+3)/2=2.5.

def get_mean(arr, x, y):
    if 1 < x <= len(arr) and 1 < y <= len(arr):

        x1 = sum(arr[:x]) / x
        y1 = sum(arr[-y:]) / y
        return (x1 + y1) / 2
    else:
        return -1