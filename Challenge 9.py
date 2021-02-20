#This problem was asked by Airbnb.

#Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or (-).

#For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# import sus
import sys

#set up function to take in array
def get_largest_non_adj_sum(array):
    #set up values to equal 0
    previous, largest = 0, 0
    #loop through arrat
    for amount in array:
        # take the amount, previous number, and largest value
        print("amount: {}; previous: {}; largest: {}".format(amount, previous, largest))
        #aseese wether the (previous and amount) make larger value then precious largest combo
        previous, largest = largest, max(largest, previous + amount)
        print("new_previous: {}; new_largest: {}".format(previous, largest))
    #return largest combo    
    return largest

print(get_largest_non_adj_sum([2, 4, 6, 8]))
print(get_largest_non_adj_sum([5, 1, 1, 5]))
