#Question 34

#This problem was asked by Quora.

#Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in 
#the word. If there is more than one palindrome of minimum length that can be made, 
#return the lexicographically earliest one (the first one alphabetically).

#For example, given the string “race”, you should return “ecarace”, since we can add three letters to it 
#(which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from “race” by 
#adding three letters, but “ecarace” comes first alphabetically.

#As another example, given the string “google”, you should return “elgoogle”.

#Answer 34

#function to check if palindrome
def is_palindrome(s):
    #does reverse = foward
    return s[::-1] == s

#fucntion to get neaeest
def get_nearest_palindrome(s):
    #if palndrom
    if is_palindrome(s):
        #return as is
        return s
    #if first letter and last letter same
    if s[0] == s[-1]:
        #then take those out and add to function of slice
        return s[0] + get_nearest_palindrome(s[1:-1]) + s[-1]
    #otherwie
    else:
        #create variable where first letter taken out and added to sliced in function
        pal_1 = s[0] + get_nearest_palindrome(s[1:]) + s[0]
        #another viarbale where last letter taken out and added to sliced in function
        pal_2 = s[-1] + get_nearest_palindrome(s[:-1]) + s[-1]
        
        #if length pasl2 lesse then pal 1 return pal2
        if len(pal_1) > len(pal_2):
            return pal_2
        #and vice versa
        elif len(pal_1) < len(pal_2):
            return pal_1
        #if length pasl2 lesse then pal 1 return pal2 and vice versa
        return pal_1 if pal_1 < pal_2 else pal_2


assert get_nearest_palindrome("racecar") == "racecar"
assert get_nearest_palindrome("google") == "elgoogle"
assert get_nearest_palindrome("egoogle") == "elgoogle"
assert get_nearest_palindrome("elgoog") == "elgoogle"
assert get_nearest_palindrome("race") == "ecarace"
