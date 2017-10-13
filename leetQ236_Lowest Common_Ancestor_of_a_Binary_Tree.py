
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data  = data
        self.left  = left
        self.right = right


def find(root, data):
    while root:
        if root.data == data:
            return root
        if root.data > data:
            root = root.left
        else:
            root = root.right


def lca(root, node1, node2):
    if root in (None, node1, node2):
        return root    

    left  = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)
    if left and right:
        return root
    else:
        return left or right 
    
    

if __name__ == '__main__':
    root = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
    node1 = find(root, 2)
    node2 = find(root, 5)
    c = lca(root, node1, node2)
    print c.data

    node1 = find(root, 5)
    node2 = find(root, 7)
    c = lca(root, node1, node2)
    print c.data 
