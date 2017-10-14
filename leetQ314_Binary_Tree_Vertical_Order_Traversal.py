'''
314. Binary Tree Vertical Order Traversal
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

For example, given below binary tree:

  3
  /\
 /  \
 9  20
    /\
   /  \
  15   7

Return vertical order traversal
[
  [9],
  [3,15],
  [20],
  [7]
]

'''

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalOrder(root):
    if not root:
        []
    from collections import defaultdict
    mp = defaultdict(list)
    queue = [(root, 0)]
    while queue:
        next_level = []
        for node, idx in queue:
            mp[idx].append(node.val)
            if node.left: next.level.append(node.left)
            if node.right: next.level.append(node.right)
        queue = next_level
    res = [mp[idx] for idx in sorted(mp)]
    print res
    return res

def __name__ == '__main__':
    root = Node(3, Node(9), Node(20, Node(15), Node(7)))
    verticalOrder(root)


