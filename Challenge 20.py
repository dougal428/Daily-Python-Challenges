#This problem was asked by Google.

#Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

#For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

#In this example, assume nodes with the same value are the exact same node objects.

#Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

#Answer 20

#create node class with a value, and a next on line value
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

#create string representation of how long along chain
    def __str__(self):
        #initiate with bracket
        string = "["
        node = self
        while node:
            #add node
            string += "{} ->".format(node.val)
            node = node.next
        #end chain
        string += "None]"
        return string

#get the next nodes
def get_nodes(values):
    next_node = None
    #for value in reversed list 
    for value in values[::-1]:
        #
        node = Node(value)
        node.next = next_node
        next_node = node

    return next_node

#get the list
def get_list(head):
    #get the node and set empty list
    node = head
    nodes = list()
    #hile node is present in chain
    while node:
        #appends node to list
        nodes.append(node.val)
        #moving to next along chain
        node = node.next
    #return list
    return nodes

#get inersection node
def get_intersection_node(list_a, list_b):
    
####create function to get list lenght of node
    def get_list_length(linked_list):
        length = 0
        node = linked_list
#######while node is present in chain
        while node:
##########add one to counter and get the next
            length += 1
            node = node.next
#########return length
        return length

#find lenth of both lists and get min
    len_a, len_b = get_list_length(list_a), get_list_length(list_b)
    min_len = min(len_a, len_b)
####go through that in range of min in boths chain and make lists of them
    for _ in range(len_a - min_len):
        list_a = list_a.next
    for _ in range(len_b - min_len):
        list_b = list_b.next
###and got thorugh both lists
    node_a = list_a
    node_b = list_b
    for _ in range(min_len):
#####and if there is interesction  return the node
        if node_a.val == node_b.val:
            return node_a
        node_a = node_a.next
        node_b = node_b.next

    return None


assert not get_intersection_node(
    get_nodes([]), get_nodes([]))
assert get_intersection_node(
    get_nodes([0, 3, 7, 8, 10]), get_nodes([99, 1, 8, 10])).val == 8
assert get_intersection_node(
    get_nodes([7, 8, 10]), get_nodes([99, 1, 8, 10])).val == 8
