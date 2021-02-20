#Question 30

#You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is 
# a unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

#Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

#For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

#Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 
#2 in the second, 
#and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

Answer 30


def calculate_trapped_water(walls):
    
    #need three elevation to trap water as othewise escape
    if len(walls) < 3:
        return 0

    #add water volume stored to
    total_water_volume = 0

    #find height of walls
    left = 0
    right = len(walls) - 1
    left_max = 0
    right_max = 0
    
    #water falls to left side
    while left <= right:
        #if left wall less than rifht
        if walls[left] < walls[right]:
            if walls[left] > left_max:
                #set left max height to that
                left_max = walls[left]
            #othewirse
            else:#add the dffrences betwween left max and left wall as water falls to left
                total_water_volume += left_max - walls[left]
            #add one to left as moved one along
            left += 1
            
        #ifleft wall more then right
        else:
            #and if current wall greater than right max
            if walls[right] > right_max:
                #set that wall to right max
                right_max = walls[right]
            else:
                #othewise add d differnce to toal vol
                total_water_volume += right_max - walls[right]
            #and minus one from right
            right -= 1
            
    #retunr toal volume
    return total_water_volume


assert calculate_trapped_water([1]) == 0
assert calculate_trapped_water([2, 1]) == 0
assert calculate_trapped_water([2, 1, 2]) == 1
assert calculate_trapped_water([4, 1, 2]) == 1
assert calculate_trapped_water([4, 1, 2, 3]) == 3
assert calculate_trapped_water([3, 0, 1, 3, 0, 5]) == 8
assert calculate_trapped_water([10, 9, 1, 1, 6]) == 10
