# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Input: root node of tree
        # Output: bool for validity

        # let's do BFS --> So far this only checks each node and children; not parents
        # we need to store left bound and right bound
        queue = [[root, float("-inf"), float("inf")]]
        while len(queue) > 0:
            item = queue.pop(0)
            node = item[0]
            left = item[1]
            right = item[2]
            if node:
                # check if node is between bounds
                # print(left, node.val, right)
                if not left < node.val < right:
                    
                    return False
                
                if node.left:
                    # set new bounds: lower remains, upper is left node's parent (cur node)
                    queue.append([node.left, left, node.val])
                if node.right:
                    # set new bounds: upper remains, lower is right node's parent (cur node)
                    queue.append([node.right, node.val, right])
        return True


        
