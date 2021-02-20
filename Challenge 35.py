#Question 35

#This problem was asked by Google.

#Given an array of strictly the characters ‘R’, ‘G’, and ‘B’, segregate the values of the array so that all the Rs 
# come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

#Do this in linear time and in-place.

#For example, given the array [‘G’, ‘B’, ‘R’, ‘R’, ‘B’, ‘R’, ‘G’], it should become [‘R’, ‘R’, ‘R’, ‘G’, ‘G’, ‘B’, ‘B’].



def swap_indices(arr, i, j):
    #get value of array index and store in tmp varaoble
    tmp = arr[i]
    #set value of array index i to array index j value
    arr[i] = arr[j]
    #set value of array index j to tmp value
    arr[j] = tmp


def pull_elements_to_front(arr, start_index, end_index, letter):
    #set i to srt index
    i = start_index
    #set j to end inex
    j = end_index
    #and last letter index to -1
    last_letter_index = -1
    
    #while i less then j
    while i < j:
        
        #if vlaue at array index i= the letter
        if arr[i] == letter:
            #then make i the last leter index
            last_letter_index = i
            #ass one to that value
            i += 1
        
        #if value at array index j not = to letter
        elif arr[j] != letter:
            #minus one from j i.e. end index
            j -= 1
            
        #otherise
        else:
            #set last letter index to i
            last_letter_index = i
            #and swap indices
            swap_indices(arr, i, j)

    return last_letter_index

#redorfer fucntion
def reorder_array(arr):
    #find last index of red
    last_index = pull_elements_to_front(arr, 0, len(arr) - 1, "R")
    #then for the green and remeber to add one to tart index fotr it
    pull_elements_to_front(arr, last_index + 1, len(arr) - 1, "G")

    return arr


assert reorder_array(['G', 'R']) == ['R', 'G']
assert reorder_array(['G', 'B', 'R']) == ['R', 'G', 'B']
assert reorder_array(['B', 'G', 'R']) == ['R', 'G', 'B']
assert reorder_array(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == [
    'R', 'R', 'R', 'G', 'G', 'B', 'B']
