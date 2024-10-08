# Write the function :
#
# def encode(str)
# that takes in a string str and replaces all the letters with their respective positions in the English alphabet.
#
# encode('abc') == '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
# encode('codewars') == '315452311819'
# encode('abc-#@5') == '123-#@5'
# String are case sensitive.

def encode(string):
    str_ = ""
    for i in string.lower():
#         if i in ('abcdefghigklmnopqrstuvwxyz'):
        if i.isalpha():
            str_ += str(ord(i)-96)
        else:
            str_ += i
    return str_