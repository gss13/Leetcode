#Practice date: 01-May-2017

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Build_BST(object):

    def array_to_bst(self, arr):
        if not arr:
            return None
        start = 0
        end = len(arr) - 1
        def bst(arr, start, end):
            if start > end:
                return None
            mid = (start + end)//2
            root = Node(arr[mid])
            root.left = bst(arr, start, mid-1)
            root.right = bst(arr, mid+1, end)
            return root
        return bst(arr, start, end)
   
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print node.data,
            self.inorder(node.right)

            
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    b = Build_BST()
    root = b.array_to_bst(arr)
    b.inorder(root)     
