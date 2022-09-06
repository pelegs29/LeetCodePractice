# 206. Reverse Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        rev = None
        while head:
            tmp = head.next
            head.next = rev
            rev = head
            head = tmp
        return rev
