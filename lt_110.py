
# Standard question need to ask information from child to make decision on root level
# Since the question itself doesn't need depth, therefore we need create a helper function to return more information from child

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        is_balanced, _ = self.isBalancedRecursive(root)
        return is_balanced

    # need helper since we need to know the depth of child
    # two information should be retured,
    # 1. boolean to represend if child itself is balanced
    # 2. the depth of child
    def isBalancedRecursive(self, root):
        # leaf condition
        if root == None:
            return True, 0
        
        # skeleton: function need to be called recursively twice
        # assign return value to meaningful variable names
        is_l_balanced, l_depth = self.isBalancedRecursive(root.left)
        is_r_balanced, r_depth = self.isBalancedRecursive(root.right)
        
        # children must be balanced
        if not is_l_balanced or not is_r_balanced:
            # 0 is just a placeholder, because we don't care about the depth
            return False, 0
        
        # depth of child only differ by no more than 1
        if abs(l_depth - r_depth) > 1:
            return False, 0
            
        return True, max(l_depth, r_depth) + 1
        