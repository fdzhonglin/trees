
# similar to question 111, leaf definition is changed a little bit
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # leaf condition: in this example, become None node condition
        if root == None:
            return False
         
        # leaf condition by problem definition: 
        if root.left == None and root.right == None:
            if root.val == sum:
                return True
            
            return False
        
        # path sum need to update before recursive call
        sum = sum - root.val
        
        # skeleton is here again :)
        if self.hasPathSum(root.left, sum):
            return True
        
        if self.hasPathSum(root.right, sum):
            return True
        
        return False
        