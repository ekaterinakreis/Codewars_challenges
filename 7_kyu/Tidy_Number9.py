# A Tidy number is a number whose digits are in non-decreasing order.
#
# Given a number, Find if it is Tidy or not .
#
# tidyNumber (12) ==> return (true)
# he number's digits { 1 , 2 } are in non-Decreasing Order (i.e) 1 <= 2 .

def tidyNumber(n):
    x = str(n)
    for i in range(0, len(x) - 1):
        if x[i] > x[i + 1]:
            return False

    return True

def tidyNumber1(n):
    l = list(str(n))
    return l == sorted(l)