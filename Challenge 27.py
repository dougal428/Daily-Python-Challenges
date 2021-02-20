#Question 27

#This problem was asked by Facebook.

#Given a string of round, curly, and square open and closing brackets, 
#return whether the brackets are balanced (well-formed).

#For example, given the string “([])”, you should return true.

#Given the string “([)]” or “((()”, you should return false.


#create dictionary of typr of bracket
brace_map = {
    ")": "(",
    "}": "{",
    "]": "["
}

#create function taking in string of brackets
def is_balanced(s):
    #create empty list
    stack = list()
    #for each charachter ins string
    for char in s:
        # if char is in the dictionary and also last part of stcak is equal to other end of that bracket
        if stack and char in brace_map and stack[-1] == brace_map[char]:
            #then remove from stack
            stack.pop()
        else:
            #1) append the charachter to the stack
            stack.append(char)
            #check if stack empty and return true if is.
    return not stack


assert is_balanced("")
assert is_balanced("{}")
assert is_balanced("([])")
assert is_balanced("([])[]({})")
assert not is_balanced("(")
assert not is_balanced("]")
assert not is_balanced("((()")
assert not is_balanced("([)]")
