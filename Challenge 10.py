#This problem was asked by Apple.

#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

#import sleep from time module
from time import sleep

#create sample function
def sample_function():
    print("hello")
    

#create scheduler function wwhich takes in function and delay time
def schedule_function(f, delay_in_ms):
    #divide delay time by 1000 to make milliseconds
    delay_in_s = delay_in_ms / 1000
    #set sleep to that time
    sleep(delay_in_s)
    #then function
    f()

schedule_function(sample_function, 10000)
