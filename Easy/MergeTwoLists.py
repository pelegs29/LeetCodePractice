# 21. Merge Two Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
    curr = temp = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            curr = list1
            list1 = list1.next
        else:
            curr.next = list2
            curr = list2
            list2 = list2.next

    if list1 or list2:
        curr.next = list1 if list1 else list2

    return temp.next
