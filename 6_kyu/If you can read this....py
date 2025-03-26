# Task
# You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).
#
# Input:
#
# If, you can read?
#
# Output:
#
# India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?
#
# Note:
#
# There is a preloaded dictionary that you can use, named NATO. It uses uppercase keys, e.g. NATO['A'] is "Alfa".
# See comments in the initial code to see how to access it in your language.
# The set of used punctuation is ,.!?.
# Punctuation should be kept in your return string, but spaces should not.
# Xray should not have a dash within.
# Every word and punctuation mark should be seperated by a space ' '.
# There should be no trailing whitespace

from preloaded import NATO # NATO['A'] == 'Alfa', etc


def to_nato(words : str) -> str:
    lst =[]
    for i in words:
        if i.upper() in NATO.keys():
            lst.append(NATO.get(i.upper()))
        else:
            if i != " ":
                lst.append(i)
    return ' '.join(lst)

# _________________________________________
to_nato1 = lambda words: ' '.join(NATO.get(char, char) for char in words.upper() if char != " ")
