class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            
            # update max_diameter if this path is longer
            self.max_diameter = max(self.max_diameter, left + right)
            
            # return height of the subtree rooted at this node
            return max(left, right) + 1

        height(root)
        return self.max_diameter
