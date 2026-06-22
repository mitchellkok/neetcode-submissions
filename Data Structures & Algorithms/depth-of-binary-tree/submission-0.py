# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Approach 1: Iterative DFS tree traversal?
        # for DFS we need a stack, storing [node, level]
        stack = [[root,0]]
        maximum = 0

        while len(stack) > 0:
            item = stack.pop()
            node = item[0]
            level = item[1]
            maximum = max(maximum, level)
            if node is not None:
                stack.append([node.left, level+1])
                stack.append([node.right, level+1])
        
        return maximum
