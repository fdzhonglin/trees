
# solution1: performance is not very good
# Array concatenation takes time.

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # Pattern: Stop when root is None
        if root == None:
            return [] 

        # Pattern: Need recurseive call on left and right 
        l_nodes = self.inorderTraversal(root.left)
        r_nodes = self.inorderTraversal(root.right)

        return l_nodes + [root.val] + r_nodes



# solution2: performance is good
# Need helper function

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        self.helper(root, result)

        return result
        

    def helper(self, root, result):
        # Pattern: Stop when root is None
        if root == None:
            return

        # Pattern: Need recurseive call on left and right 
        self.helper(root.left, result)
        result.append(root.val)
        self.helper(root.right, result)
