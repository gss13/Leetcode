
class ZigZagIterator(object):
    def __init__(self, v1, v2):
        self.queue = [x for x in (v1, v2) if x]

    def next(self):
        v = self.queue.pop(0)
        ret = v.pop(0)
        if v: self.queue.append(v)
        return ret

    def hasNext(self):
        if self.queue: return True
        return False

if __name__ == '__main__':
    v1 = [1, 2]
    v2 = [3, 4, 5, 6]
    i = ZigZagIterator(v1, v2)
    res = []
    while i.hasNext():
        res.append(i.next())
    print res
