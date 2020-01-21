

# Step 1: Use simple exampe to get familiar with question
# Use example to generate BST 
# for example: [1, 2, 3] can generate
#    1      |     1                        
#      2    |       3     
#        3  |      2                  
#     
#       2
#     1   3
#
#       3    |        3
#     2      |      1
#    1       |       2
#
# Step 2: Generate the patter from root
#     * All the number in array can be root
#     * If root is selected: 
#          - numbers smaller than root val will be left part of root, 
#          - numbers bigger than root val will be right part of root
#
# Step 3: From what we get from step 2
#     * Need a for loop for each number because all the number can be root
#     * After root is selected, the left part and right part is the same as original question
#           - This is the patter we are waiting for. We divide the array acoording to the root, and
#             for left part and right part, we will call the recursive function
#

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # corner case: don't handle in helper function. 
        # Make more sense here. 
        if n == 0:
            return []

        return self.helper(1, n)

    # Return type is tricky. Since we have multiple trees can be build for specific range,
    # the return type should be a collection of roots. I will use array here
    #
    # The function itself, it's like build_tree function.
    #
    def helper(self, start, end):
        # patter here
        if start > end: 
            # this part is error-prone, rememeber, we need a array for return type. 
            return [None]

        roots = []
        # end + 1 because range function is exclusive on stop
        for i in range(start, end+1):
            # pattern here
            l_roots = self.helper(start, i - 1)
            r_roots = self.helper(i + 1, end)

            for l_root in l_roots:
                for r_root in r_roots:
                    root = TreeNode(i)
                    root.left = l_root
                    root.right = r_root
                    roots.append(root)
        
        return roots



