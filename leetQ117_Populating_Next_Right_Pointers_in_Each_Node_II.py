'''
Q117. Populating Next Right Pointers in Each Node II
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
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
			#print node.data,
			if node.left: next_level.append(node.left)
			if node.right: next_level.append(node.right)
		cur_level = next_level
		print

def connect(root):
	while root:
		next_root = root.left if root.left else root.right
		while root:
			if (root.left and root.right):
				root.left.next = root.right
			elif (root.left and root.next):
				if root.next.left:
					root.left.next = root.next.left
				elif root.next.right:
					root.left.next = root.next.right	
			if root.right:
				if (root.next and root.next.left):
					root.right.next = root.next.left
				elif (root.next and root.next.right):
					root.right.next = root.next.right
			root = root.next
		root = next_root

if __name__ == '__main__':
	#root = Node(1, Node(2, Node(4), None), Node(3, None, Node(5)))
	root = Node(1, Node(2, Node(4, Node(7)), Node(5)), Node(3, None, Node(6, None, Node(8))))
	connect(root)
	level_order(root)