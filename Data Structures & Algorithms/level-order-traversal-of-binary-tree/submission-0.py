# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # input: root of binary tree
        # output: list of list of nodes, by level
        ret_list = []

        # Approach: we can take a BFS traversal, keeping track of the level of each node
        queue = [[root,0]] # for each element, we have [node, level]

        while len(queue) > 0:
            item = queue.pop(0)
            node = item[0]
            level = item[1]
            if node:
                queue.append([node.left, level+1])
                queue.append([node.right, level+1])

                # store this node in ret list
                while level >= len(ret_list):
                    ret_list.append([])
                ret_list[level].append(node.val)

        return ret_list
