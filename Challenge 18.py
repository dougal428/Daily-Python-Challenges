#Question 18

#This problem was asked by Google.

#Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
#For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:


'10 = max(10, 5, 2)'
'7 = max(5, 2, 7)'
'8 = max(2, 7, 8)'
'8 = max(7, 8, 7)'

#Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.



#import doublesised qeue
from collections import deque

#create function
def get_sliding_max(a, k):

    #make empty list to store values
    max_elements = list()
    
    #if not array return none
    if not a:
        return None
    #if k = to array length retturn max
    if len(a) <= k:
        return max(a)
    
    #make doublesided que
    dq = deque()
    
    #loop through array for k time
    for i in range(k):
        #while dq is true; and  while last part of deque is less than memeber of arrar[i]
        while dq and a[dq[-1]] < a[i]:
            #remove last part from array
            dq.pop()
            #append the part to deque
        dq.append(i)
        #append the maximum element to empty list
    max_elements.append(a[dq[0]])

    # loop through for range between k and length of array
    for i in range(k, len(a)):
        #while dq true and first part of dq is less than or equal to iteration minus k
        while dq and dq[0] <= i - k:
            #remove left part from q
            dq.popleft()
        #while dq is true; and  while last part of deque is less than memeber of arrar[i]
        while dq and a[dq[-1]] < a[i]:
            #remove last part from array
            dq.pop()
         #append the part to deque   
        dq.append(i)
        #append the maximum element to empty list
        max_elements.append(a[dq[0]])
     #return array
    return max_elements

get_sliding_max([10, 5, 2, 6, 7, 8], 4)
