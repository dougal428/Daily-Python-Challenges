#This problem was asked by Google.

#You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. 
#Each False boolean represents a tile you can walk on.

#Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach 
#the end coordinate from the start. If there is no possible path, then return null. 
#You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

#For example, given the following board:

#[[f, f, f, f],
#[t, t, f, t],
#[f, f, f, f],
#[f, f, f, f]]

#and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, 
#since we would need to go through (1, 2) because there is a wall everywhere else on the second row.


from copy import deepcopy
# deep copy constructs a new compound object and then, recursively, 
# inserts copies into it of the objects that are found in the original. 

# By keeping a memo dictionary of objects already copied during the current copying pass;  
# and letting user-defined classesoverride the copying operation or the set of components copied.

#create the new cahce and add to it in this function via deep copy
def add_to_cache(coordinate, cache):
    new_cache = deepcopy(cache)
    #create coordinate to enter into insert of cache
    new_cache.add("{}-{}".format(coordinate[0], coordinate[1]))
    return new_cache

#create functionto see if has been visited
def is_visited(coordinate, cache):
    return "{}-{}".format(coordinate[0], coordinate[1]) in cache


#create function to find path
def find_path(matrix, rows, cols, start, end, cache):
    #if start and end coorfinates the same return 0
    if start == end:
        return 0
    #create new cache with start coordint put in palce of the 'f'
    cache = add_to_cache(start, cache)
    
#explore the neighbour of the 'start' coordinate
    def explore_neighbour(coordinate):
        #if coordinates not visited and not comtain 't' value
        if not is_visited(coordinate, cache) and \
                matrix[coordinate[0]][coordinate[1]] != "t":
            #the  find the pant from the next coordinates
            path_length = find_path(matrix, rows, cols, coordinate, end, cache)
            #if that not none then append to empty list
            if path_length != None:
                path_lengths.append(path_length)

    #set the empty list
    path_lengths = list()
    
    # if start cooridnate row not equal to zero then move to next row up and explore neighour of that coordinate
    if start[0] != 0:
        coordinate = (start[0] - 1, start[1])
        explore_neighbour(coordinate)
    # if start cooridnate row not equal to oe less then the bumber of row then move to next row down and explore neighour of 
    #that coordinate
    if start[0] != rows - 1:
        coordinate = (start[0] + 1, start[1])
        explore_neighbour(coordinate)
    # if start cooridnate column not equal zero then move to next column up and explore neighour of that coordinate
    if start[1] != 0:
        coordinate = (start[0], start[1] - 1)
        explore_neighbour(coordinate)
    # if start cooridnate column not equal to one less then the number of columns then move to next row down and explore
    # neighour of that coordinate
    if start[1] != cols - 1:
        coordinate = (start[0], start[1] + 1)
        explore_neighbour(coordinate)
    
    #return mimums lenfth of paths plus one if not none
    return min(path_lengths) + 1 if path_lengths else None


matrix = [["f", "f", "f", "f"],
          ["t", "t", "f", "t"],
          ["f", "f", "f", "f"],
          ["f", "f", "f", "f"]]
assert find_path(matrix, len(matrix), len(
    matrix[0]), (0, 0), (0, 0), set()) == 0
assert find_path(matrix, len(matrix), len(
    matrix[0]), (1, 0), (0, 0), set()) == 1
assert find_path(matrix, len(matrix), len(
    matrix[0]), (3, 0), (0, 0), set()) == 7
assert find_path(matrix, len(matrix), len(
    matrix[0]), (3, 0), (0, 3), set()) == 6

matrix = [["f", "f", "f", "f"],
          ["t", "t", "t", "f"],
          ["f", "f", "f", "f"],
          ["f", "f", "f", "f"]]
assert find_path(matrix, len(matrix), len(
    matrix[0]), (0, 0), (0, 0), set()) == 0
assert find_path(matrix, len(matrix), len(
    matrix[0]), (1, 0), (0, 0), set()) == 1
assert find_path(matrix, len(matrix), len(
    matrix[0]), (3, 0), (0, 0), set()) == 9
assert find_path(matrix, len(matrix), len(
    matrix[0]), (3, 0), (0, 3), set()) == 6
assert find_path(matrix, len(matrix), len(
    matrix[0]), (2, 0), (3, 3), set()) == 4
