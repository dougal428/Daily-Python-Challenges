#Question 36

#This problem was asked by Dropbox.

#Given the root to a binary search tree, find the second largest node in the tree.

#Answer 36

#create node class
class Node:
    #iniate with data
    def __init__(self, data):
        self.data = data
        #has a lef and right
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def find_largest_and_parent(node):
    #set parent as none
    parent = None
    while node.right:
        #assume right node is always larger
        parent = node
        node = node.right

    return node, parent


def find_second_largest(node):
    #if no node return 0
    if not node:
        return None

    #set value to zero
    second_largest = None
    
    #if no right node
    if node.left and not node.right:
        #find 2nd largest via that route
        second_largest, _ = find_largest_and_parent(node.left)
    else:
        #find via that node
        _, second_largest = find_largest_and_parent(node)
    print("second_largest", second_largest)

    return second_largest


def test_0():
    node_a = Node(5)

    assert not find_second_largest(node_a)


def test_1():
    node_a = Node(5)
    node_b = Node(3)
    node_c = Node(8)
    node_d = Node(2)
    node_e = Node(4)
    node_f = Node(7)
    node_g = Node(9)
    node_a.left = node_b
    node_a.right = node_c
    node_b.left = node_d
    node_b.right = node_e
    node_c.left = node_f
    node_c.right = node_g

    assert find_second_largest(node_a).data == 8


def test_2():
    node_a = Node(5)
    node_b = Node(3)
    node_d = Node(2)
    node_e = Node(4)
    node_a.left = node_b
    node_b.left = node_d
    node_b.right = node_e

    assert find_second_largest(node_a).data == 4


test_0()
test_1()
test_2()
