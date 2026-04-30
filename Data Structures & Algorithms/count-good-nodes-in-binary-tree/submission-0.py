# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def matchup(node: TreeNode, max_so_far: int) -> int:
            if not node:
                return 0

            count = 0
            if node.val >= max_so_far:
                count = 1
                max_so_far = node.val

            count += matchup(node.left, max_so_far)
            count += matchup(node.right, max_so_far)
            return count

        return matchup(root, root.val)