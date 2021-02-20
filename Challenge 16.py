#This problem was asked by Twitter.

#You run an e-commerce website and want to record the last N order ids in a log. 
#Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log get_last(i): gets the ith last element from the log.i is guaranteed to 
# be smaller than or equal to N. You should be as efficient with time and space as possible.


#set up class called OrderLog
class OrderLog:
    # initiate with self, and proclaimed size
    def __init__(self, size):
        self.log = list()
        self.size = size
        
    # set string represenation
    def __repr__(self):
        return str(self.log)
    
    #set up recrodings of order via appending to list
    def record(self, order_id):
        self.log.append(order_id)
        # remove oldest order if new appendage makes it to big for log
        if len(self.log) > self.size:
            self.log = self.log[1:]
            
    #set up the taking of order from log
    def get_last(self, i):
        return self.log[-i]


log = OrderLog(5)
log.record(1)
log.record(2)
assert log.log == [1, 2]
log.record(3)
log.record(4)
log.record(5)
assert log.log == [1, 2, 3, 4, 5]
log.record(6)
log.record(7)
log.record(8)
assert log.log == [4, 5, 6, 7, 8]
assert log.get_last(4) == 5
assert log.get_last(1) == 8
