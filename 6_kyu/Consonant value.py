# Given a lowercase string that has alphabetic characters only and no spaces,
# return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".
#
# We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.
#
# For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"
#
# -- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22.
# The highest is 26.
# solve("zodiacs") = 26
#
# For the word "strength", solve("strength") = 57
# -- The consonant substrings are: "str" and "ngth" with values "str"
# and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.

def solve(s):
    s = s.split(" ")

    maximum = 0
    alphabet = '_abcdefghijklmnopqrstuvwxyz'
    for letter in s:
        total = 0
        for i in letter:
            total += alphabet.index(i)
            if total > maximum:
                maximum = total
        return maximum

def solve1(s):
    alphabet = "_abcdefghijklmnopqrstuvwxyz"
    for vowel in "aeiou":
        s = s.replace(vowel, " ")
    values = []
    for i in s.split(" "):
        sum = 0
        for letter in i:
            sum += alphabet.index(letter)
        values.append(sum)
    return max(values)