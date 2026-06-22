# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Approach: Iterate through list repeatedly, taking the smallest node possible each time

        ret_list = ListNode(None,None)
        cur = ret_list
        while len(lists) > 0:
            minimum = 9999
            min_idx = -1
            empty_lists = []
            for i in range(len(lists)):
                if lists[i] is None:
                    # empty list
                    empty_lists.append(i)
                    continue
                elif lists[i].val < minimum:
                    # keep track of the smallest found
                    minimum = lists[i].val
                    min_idx = i

            if lists[min_idx]:
                cur.next = lists[min_idx] # add to merged list
                cur = cur.next 
                lists[min_idx] = lists[min_idx].next # remove this node from linked list

            for i in empty_lists:
                # clear empty lists
                lists.pop(i)
        return ret_list.next