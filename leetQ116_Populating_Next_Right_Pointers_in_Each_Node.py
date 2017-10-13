'''
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
'''

class Node(object):
	def __init__(self, data, left=None, right=None):
		self.data  = data
		self.left  = left
		self.right = right
		self.next  = None

def level_order(root):
	cur_level = [root]
	while cur_level:
		next_level = []
		for node in cur_level:
			print node.data, '-->', node.next.data if node.next else None
			if node.left: next_level.append(node.left)
			if node.right: next_level.append(node.right)
		cur_level = next_level
		print


def connect(root):
	while root:
		left_most = root.left
		while root and root.left:
			root.left.next = root.right
			root.right.next = root.next.left if root.next else None
			root = root.next
		root = left_most


if __name__ == '__main__':
	root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
	connect(root)
	level_order(root)
