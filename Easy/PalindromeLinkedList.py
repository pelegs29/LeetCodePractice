# 234. Palindrome Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            tmp = rev
            rev = slow
            slow = slow.next
            rev.next = tmp
        if fast:
            slow = slow.next
        while rev:
            if rev.val != slow.val:
                return False
            slow = slow.next
            rev = rev.next
        return True
