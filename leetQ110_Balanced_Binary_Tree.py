#Practice date: 01-May-2017

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def level_order(root):
    cur_level = [root]
    while cur_level:
        next_level = []
        for node in cur_level:
            print node.data,
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)
        cur_level = next_level
        print


class Solution(object):
    def validate(self, root):
        if not root:
            return 0
        left  = self.validate(root.left)
        right = self.validate(root.right)
        if left < 0 or right < 0 or abs(left-right) > 1:
            return -1
        return max(left, right) + 1   
    

if __name__ == '__main__':
    #r1 = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
    #r1 = Node(1, Node(2, Node(4)), Node(3))
    r1 = Node(1, Node(2, Node(4, Node(5))), Node(3))
    v = Solution()
    result = v.validate(r1)
    level_order(r1)
    if result != -1:
        print 'Tree is height balanced'
    else:
        print 'Tree is NOT height balanced'
