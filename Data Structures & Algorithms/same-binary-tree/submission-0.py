# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # inputs: two trees p and q
        # output: bool showing if they match

        # Approach: iterative using two stacks
        stack_p = [p]
        stack_q = [q]

        while len(stack_p) > 0 and len(stack_q) > 0:
            node_p = stack_p.pop()
            node_q = stack_q.pop()
            if node_p and node_q:
                if node_p.val != node_q.val:
                    return False

            if node_p:
                stack_p.append(node_p.left)
                stack_p.append(node_p.right)
            if node_q:
                stack_q.append(node_q.left)
                stack_q.append(node_q.right)

            if len(stack_q) != len(stack_p):
                return False
        
        return True