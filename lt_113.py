# same as question 112, need to save the result
# there is two way to store result crossing tree level
# 1. Global variable, not good coding style, you should not use it.
# 2. referenced variable in parameter
# I will use option 2, which means I need change the signature of the function, which means no help function will be created
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.pathSumRecursive(root, sum, [], result)
        return result
    
    # since I put result in parameter, there is no return information needed
    # path_nodes hold the all the nodes in the path from root to leaf
    def pathSumRecursive(self, root, sum, path_nodes, result):
        # leaf condition: in this example, become None node condition
        if root == None:
            return
        
        # put current node into path
        path_nodes.append(root.val)
        
        # leaf condition by problem definition
        if root.left == None and root.right == None: 
            if root.val == sum:
                # need to make an copy since path_nodes will dynamically change during the call
                result.append(path_nodes[:])
            path_nodes.pop()
            return
        
        # skeleton here: go left child and right child to find all        
        sum = sum - root.val
        self.pathSumRecursive(root.left, sum, path_nodes, result)
        self.pathSumRecursive(root.right, sum, path_nodes, result)
        
        # Don't forget pop root, since the path on upper level should not contain this root 
        path_nodes.pop()