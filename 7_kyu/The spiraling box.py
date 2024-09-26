# Given two positive integers m (width) and n (height),
# fill a two-dimensional list (or array) of size m-by-n in the following way:
#
# (1) All the elements in the first and last row and column are 1.
#
# (2) All the elements in the second and second-last row and column are 2, excluding the elements from step 1.
#
# (3) All the elements in the third and third-last row and column are 3, excluding the elements from the previous steps.

def create_box(w, h):
    arr = []
    for num in range(h):

        temp = []

        for num2 in range(w):
            temp.append(min(num2 + 1, num + 1, w - num2, h - num))

        arr.append(temp)
    return arr



