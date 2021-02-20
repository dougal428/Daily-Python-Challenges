#Question 24

#This problem was asked by Google.

#Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

#Design a binary tree node class with the following methods:

#is_locked, which returns whether the node is locked lock, which attempts to lock the node. 
#If it cannot be locked, then it should return false. Otherwise, it should lock it and return true. 
#unlock, which unlocks the node. If it cannot be unlocked, then it should return false. 
#Otherwise, it should unlock it and return true. 
#You may augment the node to add parent pointers or any other property you would like. 
#You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. 
#Each method should run in O(h), where h is the height of the tree.


#create function to see if node's parent is locked
def is_parent_locked(node):
    #if no node return false
    if not node.parent:
        return False
    #if is locked reurn true
    elif node.parent.locked:
        return True
    #check to see if parent node true/false
    return is_parent_locked(node.parent)

#create function to unlock/lock node by  modifituing the key to a 0 or -1 value
def update_parent(node, enable_locks):
    #set incriment to increase if enable the lock onto truw
    increment = 1 if enable_locks else -1
    #if parent there
    if node.parent:
        #modify locked descendant
        node.parent.locked_descendants += increment
        #then modufy the parent via same functio 
        update_parent(node.parent, enable_locks)

#create the node class, take in lock value and it's parent
class Node:
    
    #initiate node with the parent/child info and lcok value
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None
        self.locked = False
        self.locked_descendants = 0
        
   #create a string reprentation of node
    def __str__(self):
        return "val={}; locked={}; locked_descendants={}".format(
            self.val, self.locked, self.locked_descendants)
    
   #create attribute to  lock
    def lock(self):
        #false if not
        if is_parent_locked(self) or self.locked_descendants:
            return False
        else:
            #true if so
            self.locked = True
            update_parent(node=self, enable_locks=True)
            return True

        #create attribute to unlock
    def unlock(self):
        #if parent/ child locked retun false
        if is_parent_locked(self) or self.locked_descendants:
            return False
        else:
            self.locked = False
            update_parent(node=self, enable_locks=False)
            return True
        
    #check to see if locked
    def is_locked(self):
        return self.locked


a = Node("a", None)
b = Node("b", a)
c = Node("c", a)
d = Node("d", b)
e = Node("e", b)
f = Node("f", c)
g = Node("g", c)

assert b.lock()
assert b.is_locked()
assert c.lock()
assert b.unlock()
assert not b.is_locked()
assert d.lock()

assert not g.lock()
assert c.unlock()
assert g.lock()

assert f.lock()
assert e.lock()
assert a.locked_descendants == 4
assert b.locked_descendants == 2
assert c.locked_descendants == 2
