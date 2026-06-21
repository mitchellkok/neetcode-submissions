# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1: use a temporary node to reverse nodes as we visit
        # 1 > 2 > 3 > 4
        # prev = 1, cur = 2, temp = cur.next, cur.next = prev, prev = cur, cur = temp

        prev = None
        cur = head
        while cur is not None:
            temp = cur.next
            
            cur.next = prev
            prev = cur
            cur = temp

        return prev