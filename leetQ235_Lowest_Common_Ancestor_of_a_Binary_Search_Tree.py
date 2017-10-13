
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data  = data
        self.left  = left
        self.right = right

def find(root, node):
    while root:
        if root.data == node:
            return root
        if root.data > node:
            root = root.left
        else:
            root = root.right

def lca(root, node1, node2):
    while root:
        if node1.data < root.data > node2.data:
            root = root.left
        elif node1.data > root.data < node2.data:
            root = root.right
        else:
            return root


if __name__ == '__main__':
    root = Node(6, Node(2, Node(0), Node(4, Node(3), Node(5))), Node(8, Node(7), Node(9)))
    node1 = find(root, 4)
    node2 = find(root, 2)
    c = lca(root, node1, node2)
    print c.data
    node1 = find(root, 3)
    node2 = find(root, 5)
    c = lca(root, node1, node2)
    print c.data        
