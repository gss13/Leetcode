'''
653. Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two 
elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

'''

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget_dfs(root, k):
    cache = set()
    def dfs(root, k):
        if not root:
            return False
        if k - root.val in cache:
            return True
        cache.add(root.val)
        return dfs(root.left, k) or dfs(root.right, k)
    return dfs(root, k)


def findTarget_bfs(root, k):
    if not root:
        return False
    cache = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if k - node.val in cache:
            return True
        cache.add(root.val)
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return False


if __name__ == '__main__':
    root = Node(5, Node(3, Node(2), Node(4)), Node(6, None, Node(7)))
    k = 9
    print findTarget_dfs(root, k), ' : ', k, ':: DFS' 
    print findTarget_bfs(root, k), ' : ', k, ':: BFS'
    k = 28
    print findTarget_dfs(root, k), ' : ', k, ':: DFS'
    print findTarget_bfs(root, k), ' : ', k, ':: BFS'
