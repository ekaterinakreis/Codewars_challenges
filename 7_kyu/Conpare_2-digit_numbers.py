# You are given 2 two-digit numbers. You should check if they are similar by comparing their numbers,
# and return the result in %.
#
# Example:
#
# compare(13,14)=50%;
# compare(23,22)=50%;
# compare(15,51)=100%;
# compare(12,34)=0%.

def compare(a, b):
    aa = sorted(str(a))
    bb = sorted(str(b))
    if aa == bb:
        return "100%"
    elif aa[0] in bb or aa[1] in bb:
        return "50%"
    else:
        return "0%"

def compare1(a, b):
    if str(a) == str(b) or str(a) == str(b)[::-1]:
        return "100%"
    elif str(a)[0] not in str(b) and str(a)[-1] not in str(b):
        return "0%"
    return "50%"