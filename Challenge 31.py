
#This problem was asked by Google.

#The edit distance between two strings refers to the minimum number of character insertions, deletions,
#and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting”
#is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

#Given two strings, compute the edit distance between them.

#get the inputs
def get_edit_distance(s1, s2):
    #if same then none
    if s1 == s2:
        return 0
    
    #else if none in one return length of the other
    elif not s1:
        return len(s2)
    elif not s2:
        return len(s1)
    
    #if first letter same i both
    if s1[0] == s2[0]:
        #then parse out and put rest into the function
        return get_edit_distance(s1[1:], s2[1:])

    #else add 1
    return 1 + \
        #and min value of the following
        min(
        get_edit_distance(s1[1:], s2),      # deletion from s1 and into the funtion
        get_edit_distance(s1, s2[1:]),      # addition to s1 and into the function
        get_edit_distance(s1[1:], s2[1:]))  # modification to s1 and into funtion


assert get_edit_distance("", "") == 0
assert get_edit_distance("a", "b") == 1
assert get_edit_distance("abc", "") == 3
assert get_edit_distance("abc", "abc") == 0
assert get_edit_distance("kitten", "sitting") == 3
