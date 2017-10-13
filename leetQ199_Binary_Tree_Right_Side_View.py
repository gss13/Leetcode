#Practice date: 03-May-2017

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data  = data
        self.left  = left
        self.right = right

def right_view(root):
    view = []
    cur_level = [root]
    while cur_level:
        view.append(cur_level[-1].data)
        next_level = []
        for node in cur_level:
            print node.data,
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)
        cur_level = next_level
        print
    print 'Right view tree: {}'.format(view)


if __name__ == '__main__':
    root = Node(1, Node(2, None, Node(4, Node(6, None, Node(7)))), Node(3, Node(5)))
    right_view(root)
