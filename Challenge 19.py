#Question 19

#This problem was asked by Facebook.

#A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while 
#ensuring that no two neighboring houses are of the same color.

#Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, 
#return the minimum cost which achieves this goal.

#Answer 19

#import sys module
import sys

#cretae functions which takes in matrix, and other input where num houses all in matrix, and colours just in the row
def get_minimum_painting_cost(cost_matrix, num_houses, num_colors):
    #return 0 if no matric
    if not cost_matrix:
        return 0
    
#set house price to 0
    prev_house_min = 0
#set indedx to -1 so works
    prev_house_min_index = -1
#set previouse house price to 0
    prev_house_second_min = 0
    
#loop through the matrix
    for i in range(num_houses):
        #make variables maximum int size
        curr_house_min = sys.maxsize
        curr_house_second_min = sys.maxsize
        #set index to 0
        curr_house_min_index = 0
        
#loop through the row
        for j in range(num_colors):
        #if index equal to value in colours
            if prev_house_min_index == j:
                #then make coord  in matrix plus the previos house second min
                cost_matrix[i][j] += prev_house_second_min
            else:
                #otherwise make coord  in matrix plus the previos house  min
                cost_matrix[i][j] += prev_house_min

            #if current hose min greater then coordinate value in matrux
            if curr_house_min > cost_matrix[i][j]:
                #then set the second min of house to old minmum
                curr_house_second_min = curr_house_min
                #and the new min to the coord value in matrix
                curr_house_min = cost_matrix[i][j]
                #and replade the index woth the j row index
                curr_house_min_index = j
            #but if curr house min less or same then, and the second min value grreater then coord in matirx
            elif curr_house_second_min > cost_matrix[i][j]:
                #make second min value the same as coord in cost matrix
                curr_house_second_min = cost_matrix[i][j]
                
        #rearrange prev house min the current house min
        prev_house_min = curr_house_min
        #second minum the other second minum
        prev_house_second_min = curr_house_second_min
        #and the index new one as well
        prev_house_min_index = curr_house_min_index

    #return min value in matrix
    return min(cost_matrix[num_houses - 1])



cost_matrix = \
    [[7, 7, 8, 6, 1, 2],
     [5, 6, 7, 2, 4, 3],
     [1, 7, 4, 9, 7, 6],
     [10, 1, 4, 5, 9, 1],
    [10, 1, 4, 5, 9, 8],
    [10, 1, 4, 5, 9, 9],
         [1, 7, 4, 9, 7, 6],]
get_minimum_painting_cost(cost_matrix,
                                 len(cost_matrix), len(cost_matrix[0]))
