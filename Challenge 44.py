#Question 44

#This problem was asked by Google.

#We can determine how “out of order” an array A is by counting the number of inversions it has. 
#Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. 
#That is, a smaller element appears after a larger element.

#Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

#You may assume each element in the array is distinct.

#For example, a sorted list has zero inversions. T
#he array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). 
#The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

#Answer 44


def merge(a_with_inv, b_with_inv):
    #set indexes to 0
    i, k = 0, 0
    #create empty list
    merged = list()
    
    #get index and value of a
    a, a_inv = a_with_inv
    #get index and value of b
    b, b_inv = b_with_inv
    #get inversions
    inversions = a_inv + b_inv

    #while index less then length of array
    while i < len(a) and k < len(b):
        #if value in a less then value in b
        if a[i] < b[k]:
            #append a value to merged
            merged.append(a[i])
            #add one to i
            i += 1
        #othewrise
        else:
            #add b value to merged
            merged.append(b[k])
            #add lngthe of sliced a array to inversi9n
            inversions += len(a[i:])
            #add one to k
            k += 1

    #while i less then a lenfth
    while i < len(a):
        #append valye to merged
        merged.append(a[i])
        #add one
        i += 1
    #same for k
    while k < len(b):
        merged.append(b[k])
        k += 1

    #return merged list and inversions
    return merged, inversions


#sort merged list function
def merge_sort(arr):
    if not arr or len(arr) == 1:
        return arr, 0

    #get mid value
    mid = len(arr) // 2
    #perform merged lsit function on sliced arrays at mid
    merged_array, inversions = merge(
        merge_sort(arr[:mid]), merge_sort(arr[mid:]))
    
    #return values from fucntion
    return merged_array, inversions


#count inversiosn in array
def count_inversions(arr):
    _, inversions = merge_sort(arr)
    return inversions


assert count_inversions([1, 2, 3, 4, 5]) == 0
assert count_inversions([2, 1, 3, 4, 5]) == 1
assert count_inversions([2, 4, 1, 3, 5]) == 3
assert count_inversions([2, 6, 1, 3, 7]) == 3
assert count_inversions([5, 4, 3, 2, 1]) == 10
