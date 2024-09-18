# DropCaps means that the first letter of the starting word of the paragraph should be in caps and the remaining
# lowercase, just like you see in the newspaper.
#
# But for a change, let"s do that for each and every word of the given String.
# Your task is to capitalize every word that has length greater than 2, leaving smaller words as they are.
# should work also on Leading and Trailing Spaces and caps.
#
# "apple"            => "Apple"
# "apple of banana"  => "Apple of Banana"
# "one   space"      => "One   Space"
# "   space WALK   " => "   Space Walk   "
# Note: you will be provided atleast one word and should take string as input and return string as output.

def drop_cap(words):
    w = words.split(" ")
    str = words[:]

    for i in w:
        if len(i) > 2:
            str = str.replace(i, i.title(), 1)

    return str

def drop_cap(str_):
    return ' '.join( w.capitalize() if len(w) > 2 else w for w in str_.split(' ') )

def drop_cap(str_):
    arr = str_.split(' ')
    arr = [i[0].upper() + i[1:].lower() if len(i) > 2 else i for i in arr]
    return ' '.join(arr)