class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        result = [0]
        self.sumNumbersRecursive(root, 0, result)
        
        return result[0]
    
    # Need collect all the information of paths from root to leaf. This means we need variable available on
    # these paths. We have two choices here:
    #   1. Global variable, not good coding style, ignore it.
    #   2. Function argument, I will use this way. For this function, I use 'result' of argument. I need a 
    # to collection information, for simplicity, I use first element of array. 
    #
    # Since we need to calculate the number of the path, therefore, we need to pass down information from root,
    # therefore, another argument will be added to the path, here I use 'num_so_far'
    #
    # I don't need return anything since I collect info from argument `result`
    def sumNumbersRecursive(self, root, num_so_far, result):
        # stop condition 
        if root is None:
            return
        
        num_so_far = num_so_far * 10 + root.val
        
        # leaf condition
        if root.left is None and root.right is None:
            result[0] += num_so_far
            return
        
        # skeleton
        self.sumNumbersRecursive(root.left, num_so_far, result)
        self.sumNumbersRecursive(root.right, num_so_far, result)