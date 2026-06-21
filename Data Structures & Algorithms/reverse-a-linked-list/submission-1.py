# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1: use a temporary node to reverse nodes as we visit
        # 1 > 2 > 3 > 4
        # prev = None, cur = 1, temp = cur.next, cur.next = prev, prev = cur, cur = temp

        prev = None
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur # return this because it holds the last non-None node
            cur = temp

        return prev