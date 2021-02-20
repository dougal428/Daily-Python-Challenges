#Question 40

#This problem was asked by Google.

#Given an array of integers where every integer occurs three times except for one integer, which only occurs once, 
#find and return the non-duplicated integer.

#For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

#Do this in $O(N)$ time and $O(1)$ space.

#Answer 40


WORD_SIZE = 32

#function takes the array
def get_non_duplicated_number(arr):
    
    #set non duplicate count to 0
    non_duplicate = 0

    #loop through
    for i in range(0, WORD_SIZE):
        #set position bits to 0
        sum_i_position_bits = 0
        #set x to 1 and peform bitwise left shift to i
        x = 1 << i
        
        #loop through array
        for j in range(len(arr)):
            #if array index and x true
            if arr[j] & x:
                #add one to psoition bits
                sum_i_position_bits += 1

        #if psotion bit divisuble by 3
        if sum_i_position_bits % 3:
            #then set non duplicate to i through a Bitwise OR on operands and assign value to left operand
            non_duplicate |= x

    #return no duplicate
    return non_duplicate


assert get_non_duplicated_number([6, 1, 3, 3, 3, 6, 6]) == 1
assert get_non_duplicated_number([13, 19, 13, 13]) == 19
