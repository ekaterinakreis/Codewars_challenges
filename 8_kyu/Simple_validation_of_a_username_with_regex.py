# Write a simple regex to validate a username. Allowed characters are:
#
# lowercase letters,
# numbers,
# underscore
# Length should be between 4 and 16 characters (both included).

import re

def validate_usr(username):
    pattern = r'[a-z0-9_]{4,16}'
    x = re.fullmatch(pattern, username)
    return bool(x)
