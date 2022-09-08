# 237. Delete Node in a Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(self, node):
    middle = node.next
    node.val = middle.val
    node.next = middle.next
