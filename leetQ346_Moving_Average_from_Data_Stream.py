'''
346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of 
all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''


from collections import deque

#Method-1: Using deque container
class Moving_Average_Deque(object):
    def __init__(self, size):
        self.pipe = deque([], size)
        self.size = size
        self.sum = 0

    def next(self, val):
        if len(self.pipe) < self.size:
            self.sum += val
            self.pipe.append(val)
            return self.sum/float(len(self.pipe))
        self.sum = self.sum - self.pipe[0] + val
        self.pipe.append(val)
        return self.sum/float(self.size)


#Method-2: Using Circular Array
class Moving_Average_Circular_Array(object):
    def __init__(self, size):
        self.pipe = [0] * size
        self.size = size
        self.idx = 0
        self.sum = 0

    def next(self, val):
        self.sum = self.sum - self.pipe[self.idx % self.size] + val
        self.pipe[self.idx % self.size] = val
        self.idx += 1 # FIXME: This can cause buffer overflow. You should consider resetting logic
        return self.sum/float(min(self.size, self.idx)) 

if __name__ == '__main__':
    m1 = Moving_Average_Deque(4)
    for i in xrange(1, 11):
        print m1.next(i)
    print '-'*30 
    m2 = Moving_Average_Circular_Array(4)
    for i in xrange(1, 11):
        print m2.next(i)
