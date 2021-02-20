#Question 42

#This problem was asked by Google.

#Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. 
#If such a subset cannot be made, then return null.

#Integers can appear more than once in the list. You may assume all numbers in the list are positive.

#For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

#Answer 42

#function to take in values
def get_subset_for_sum(arr, k):

    if len(arr) == 0:
        return None

    #if value in array = k 
    if arr[0] == k:
        #return that
        return [arr[0]]

    #take fist value out and put that into function
    with_first = get_subset_for_sum(arr[1:], k - arr[0])
    #if true
    if with_first:
        #return first with second value
        return [arr[0]] + with_first
    else:
        #else go through function without first
        return get_subset_for_sum(arr[1:], k)


assert not get_subset_for_sum([], 1)
assert get_subset_for_sum([12, 1, 61, 5, 9, 2], 24) == [12, 1, 9, 2]
assert get_subset_for_sum([12, 1, 61, 5, 9, 2], 61) == [61]
assert get_subset_for_sum([12, 1, 61, 5, -108, 2], -106) == [-108, 2]
