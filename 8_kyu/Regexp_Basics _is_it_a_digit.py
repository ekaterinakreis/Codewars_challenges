# Implement String#digit?
# (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9),
# false otherwise.

import re

def is_digit(n):
    if n == "" : return False
    pattern = '\d'
    return bool(re.fullmatch(pattern, n))