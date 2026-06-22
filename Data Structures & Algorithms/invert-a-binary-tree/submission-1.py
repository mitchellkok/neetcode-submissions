# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # # Approach 1: Recursive, because each subtree represents the same problem

        # # Base Case:
        # if not root:
        #     return None
        
        # tmp_node = self.invertTree(root.left)
        # root.left = self.invertTree(root.right)
        # root.right = tmp_node

        # return root

        # Approach 2: BFS
        # For BFS, we want to use a queue
        queue = []
        queue.append(root)

        while len(queue) > 0:
            node = queue.pop(0)
            if node is not None:
                tmp_node = node.left
                node.left = node.right
                node.right = tmp_node

                queue.append(node.left)
                queue.append(node.right)

        return root
