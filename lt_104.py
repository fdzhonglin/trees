# standard traversal problem
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # leaf condition
        if root == None:
            return 0
        
        # skeleton, since function has return, need to assign variables for following usage
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
     
        # this is according to the definition
        return max(left_depth, right_depth) + 1