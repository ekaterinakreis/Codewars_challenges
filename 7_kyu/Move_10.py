# Move every letter in the provided string forward 10 letters through the alphabet.
#
# If it goes past 'z', start again at 'a'.
#
# Input will be a string with length > 0.

def move_ten(st):
    str = ''

    for i in st:
        char = ord(i) + 10
        if char > 122:
            str += chr(char - 26)
        else:
            str += chr(char)
    return str