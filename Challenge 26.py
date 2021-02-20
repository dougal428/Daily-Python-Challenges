#Question 26

#This problem was asked by Google.

#Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller 
#than the length of the list.

#The list is very long, so making more than one pass is prohibitively expensive.

#Do this in constant space and in one pass.

#Answer 26

#create node class which has a vlue and next in place value
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        
#create string prepresenations
    def __str__(self):
        #take bracket
        string = "["
        #then the node
        node = self
        #while a node
        while node:
            #insert node
            string += "{} ->".format(node.val)
            #move onto necx node
            node = node.next
        #end bracket
        string += "None]"
        return string

#get nodes functon-take in list of values
def get_nodes(values):
    #set next to none
    next_node = None
    #loop through reverese list of values
    for value in values[::-1]:
        #get the nodes
        node = Node(value)
        node.next = next_node
        next_node = node

    return next_node

#create list of fucntions
def get_list(head):
    node = head
    #create empty list
    nodes = list()
    while node:
        #append to node to list
        nodes.append(node.val)
        node = node.next
    return nodes

#removes the kth last from Node string of values
def remove_kth_last(head, k):
    if not head or not k:
        return head

    #set dummy node to none
    dummy = Node(None)
    #net node is first node
    dummy.next = head
    #runner is first node
    runner = head
    
    #loop through in k times
    for _ in range(k):
        # move runner to next node
        runner = runner.next

    #and set current node to the dummy
    current_node = dummy
    #while there is  next node
    while runner:
        #move runner to the next
        runner = runner.next
        #move current node to next
        current_node = current_node.next
        
    #move the current node next along
    current_node.next = current_node.next.next
    
    #and teturn the node next to dummy
    return dummy.next


assert get_list(remove_kth_last(
    get_nodes([]), 1)) == []
assert get_list(remove_kth_last(
    get_nodes([0, 3, 7, 8, 10]), 2)) == [0, 3, 7, 10]
assert get_list(remove_kth_last(
    get_nodes([7, 8, 10]), 3)) == [8, 10]

x = (remove_kth_last(get_nodes([7, 8, 10]),2))
