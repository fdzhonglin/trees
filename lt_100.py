class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # leaf condition 1:
        if p == None and q == None:
            return True
        # leaf condition 2:
        if p == None or q == None:
            return False
        
        # check current level value
        # comparing nodes in pre order area can boost performance a little bit
        if p.val != q.val:
            return False
        
        # skeleton, call left and right nodes here. 
        # since the return value is boolean type, return early is better.
        if not self.isSameTree(p.left, q.left):
            return False
        
        if not self.isSameTree(p.right, q.right):
            return False
        
        # All matched, therefore return true.
        return True