class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []  # list of lists per level

        def dfs(node: Optional[TreeNode], level: int):
            if not node:
                return
            # make sure there is a list for this level
            if len(result) <= level:
                result.append([])
            result[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return result