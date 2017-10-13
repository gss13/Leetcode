'''
206. Reverse Linked List

Reverse a singly linked list.
'''

#Node class definition for single linked list
class Node(object):
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

def traverseLL(head):
    cur = head
    while cur:
        print cur.val, 
        cur = cur.next
    print

def reverseLL(head):
    cur = head
    prev = None
    while cur:
        next_cur = cur.next
        cur.next = prev
        prev = cur
        cur = next_cur
    return prev


if __name__ == '__main__':
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print 'Input linked list:'
    traverseLL(head)
    r = reverseLL(head)
    print 'Reversed linked list:'
    traverseLL(r)
