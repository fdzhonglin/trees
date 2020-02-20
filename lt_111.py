class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # leaf condition
        if root == None:
            return 0
        
        # according to definition, node with two leaf childen is one
        if root.left == None and root.right == None:
            return 1
        
        # None node is not leaf node, therefore only consider right path
        if root.left == None:
            return self.minDepth(root.right) + 1
        
        # same as left
        if root.right == None:
            return self.minDepth(root.left) + 1
        
        # back to normal skeleton now :)
        # skeleton: call function recursively twice for left and right
        l_min_depth = self.minDepth(root.left)
        r_min_depth = self.minDepth(root.right)
        
        return min(l_min_depth, r_min_depth) + 1