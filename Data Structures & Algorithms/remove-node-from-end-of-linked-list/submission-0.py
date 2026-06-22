# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Approach: two passes

        # first pass: Find length of ll
        cur = head
        count = 0

        while cur:
            cur = cur.next
            count += 1


        cur = head
        ret = prev = ListNode(None, cur)
        count_2 = 0
        while cur:
            print(cur.val, count_2, count, n)
            if n == 1 and count_2 == count - n:
                print("\there1")
                prev.next = None
            elif count_2 == count - n:
                print("\there2")
                prev.next = cur.next
            prev = prev.next
            cur = cur.next
            count_2 += 1

        return ret.next