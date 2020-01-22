
# Step 1: use example to focus on root
#         5   
#     3       8
#   2   4    7  9
#
# step 2: for root, if you want to decide if it's bst:
#    * left and right childs both should be bst too.
#    * root val should be bigger than all the nodes of left, which is left_max
#    * root val should be smaller than all the nodes of right, which is right_min
#
# Step 3: Write code

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        valid_bst, _, _ = self.isValidBST_recursieve(root)
        return valid_bst


    # Return information: is child bst or not, min val of all nodes under root, max val of all nodes under root
    def isValidBST_recursieve(self, root):
        if not root:
            return True, None, None

        l_bst, l_min, l_max = self.isValidBST_recursieve(root.left)
        r_bst, r_min, r_max = self.isValidBST_recursieve(root.right)

        # check child first
        if not l_bst or not r_bst:
            return False, None, None

        # check left part
        # corner case is l_max could be None
        if l_max != None and root.val <= l_max:
            return False, None, None

        # Check right part
        # corner case is r_min counld be None
        if r_min != None and root.val >= r_min:
            return False, None, None

        # corner case for left child is None
        if l_min == None:
            l_min = root.val

        # corner case for right child is None
        if r_max == None:
            r_max = root.val

        # we need return the min and max value for current root
        # because current root could be either left child of parent or 
        # right child of parent. Therefore, we should return the range.
        return True, l_min, r_max

        
    
        