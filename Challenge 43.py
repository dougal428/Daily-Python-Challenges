#Question 43

#This problem was asked by Amazon.

#Implement a stack that has the following methods:

# 1 -push(val), which pushes an element onto the stack

# 2- pop(), which pops off and returns the topmost element of the stack. 
#   If there are no elements in the stack, then it should throw an error or return null.

# 3- max(), which returns the maximum value in the stack currently. If there are no elements in the stack, 
#    then it should throw an error or return null.

#    Each method should run in constant time.

#Answer 43

#create class
class Stack:
    
    #iniate it
    def __init__(self):
        self.stack = []
        self.max_stack = []

    #create push function takes in a value
    def push(self, val):
        #append the value
        self.stack.append(val)
        #if no max value or value is greater then maz
        if not self.max_stack or val > self.stack[self.max_stack[-1]]:
            #append that to max
            self.max_stack.append(len(self.stack) - 1)

    #create pop function
    def pop(self):
        #if empty 
        if not self.stack:
            #return none
            return None
        #if length of stack -1 is equl to max stack bottom value
        if len(self.stack) - 1 == self.max_stack[-1]:
            #pop off max stack value
            self.max_stack.pop()

        #and return stack top value
        return self.stack.pop()

    #create max function
    def max(self):
        #if empty
        if not self.stack:
            #reryrn none
            return None
        #return max value of stack
        return self.stack[self.max_stack[-1]]


s = Stack()
s.push(1)
s.push(3)
s.push(2)
s.push(5)
assert s.max() == 5
s.pop()
assert s.max() == 3
s.pop()
assert s.max() == 3
s.pop()
assert s.max() == 1
s.pop()
assert not s.max()

s = Stack()
s.push(10)
s.push(3)
s.push(2)
s.push(5)
assert s.max() == 10
s.pop()
assert s.max() == 10
s.pop()
assert s.max() == 10
s.pop()
assert s.max() == 10
s.pop()
assert not s.max()
