#This problem was asked by Facebook.

#Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.


#import trandom
from random import random

#set a counter to 0 and element to none
count_so_far = 0
result = None

#create function with variable the stream of elements
def pick_random_element(x):
    #make the counter and result/element global
    global count_so_far, result
    #add one to count
    count_so_far += 1

    print(count_so_far)
    
    #if counter equal to one  the result = element
    if count_so_far == 1:
        result = x
        
    else:
        # otherwise create random value
        random_value = int(count_so_far * random())
        #if random value one less then the counter result = element
        if random_value == count_so_far - 1:
            result = x

    return result


sample_stream = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for index, element in enumerate(sample_stream):
    random_element = pick_random_element(element)
    print("Random element of the first {} is {}".format(index + 1, random_element))
