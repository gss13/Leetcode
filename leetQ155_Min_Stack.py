#practice date: 02-May-2017

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        if self.is_empty():
            self.stack.append((item, item))
        else:
            minn = self.get_min()
            if item > minn:
                self.stack.append((item, minn))
            else:
                self.stack.append((item, item))
            
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()[0]
    
    def top(self):
        return self.stack[-1][0]

    def get_min(self):
        return self.stack[-1][1]

    def is_empty(self):
        return self.stack == []



if __name__ == '__main__':
    s = Stack()
    s.push(7)
    s.push(8)
    s.push(5)
    s.push(6)
    s.push(0)
    s.push(3)
    s.push(2)
    print 'TOP = ', s.top()
    print 'MIN = ', s.get_min()
    print '-'*10
    s.pop()
    s.pop()
    print 'TOP = ', s.top()
    print 'MIN = ', s.get_min()
    print '-'*10
    s.pop()
    print 'TOP = ', s.top()
    print 'MIN = ', s.get_min()
