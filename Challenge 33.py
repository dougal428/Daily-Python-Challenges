#Question 33

#This problem was asked by Microsoft.

#Compute the running median of a sequence of numbers. That is, given a stream of numbers, 
#print out the median of the list so far on each new element.

#Recall that the median of an even-numbered list is the average of the two middle numbers.

#For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2


import heapq as hq


def get_running_medians(arr):
    if not arr:
        return None

    min_heap = list()
    max_heap = list()
    medians = list()

    #loop through array
    for x in arr:
        #add element to min heap
        hq.heappush(min_heap, x)
        #if min heap longer than max heap plys one
        if len(min_heap) > len(max_heap) + 1:
            #samllest-large-elemt equal to min heap removed at index 1
            smallest_large_element = hq.heappop(min_heap)
            #push that value as negative into max heap
            hq.heappush(max_heap, -smallest_large_element)
        
        #if length of heaps the same
        if len(min_heap) == len(max_heap):
            #then calcualate median
            median = (min_heap[0] - max_heap[0]) / 2
        #otherwise
        else:
            #median is min heap at index 0
            median = min_heap[0]
        #append median to list
        medians.append(median)

    #return medians
    return medians


assert not get_running_medians(None)
assert not get_running_medians([])
assert get_running_medians([2, 5]) == [2, 3.5]
assert get_running_medians([3, 3, 3, 3]) == [3, 3, 3, 3]
assert get_running_medians([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]
