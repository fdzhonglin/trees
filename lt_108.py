# standard divide and conquer
# Choose a root which can divide array into left part and right part
# Best choice of root should be middle one which make the tree balanced.
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # leaf condition
        if len(nums) == 0:
            return None
        
        # skeleton: recursively call function twice to generate left part and right part
        root_index = len(nums) / 2
        left_root = self.sortedArrayToBST(nums[:root_index])
        # Right part should not include root_index, therefore + 1
        right_root = self.sortedArrayToBST(nums[root_index + 1:])
        
        # generate Root
        root_val = nums[root_index]
        root = TreeNode(root_val)
        root.left = left_root
        root.right = right_root
        
        # return to up level
        return root