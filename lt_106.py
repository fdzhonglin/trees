# Same as 105, concept is the same. Just use root from postorder to divide inorder
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # leaf condition
        if len(postorder) == 0:
            return None
        
        # last element in postorder is the root of the tree
        # -1 is python index to represent last element
        root_val = postorder[-1]

        # with index of root_val in inorder array will divide the array into left part and right part
        index = -1
        for i in range(len(inorder)):
            if inorder[i] == root_val:
                index = i
                break
        
        # skeleton: generate left root and right root
        # Caveat: the index is tricky to make right, better to use example to make it right
        #                            |
        #                           \|/
        # postorder   [9, 15, 7, 20, 3]
        #           
        #                |
        #               \|/
        # inorder    [9, 3, 15, 20, 7]
        left_root = self.buildTree(inorder[:index], postorder[:index])
        right_root = self.buildTree(inorder[index+1:], postorder[index:-1])
        
        # build tree now
        root = TreeNode(root_val)
        root.left = left_root
        root.right = right_root
        
        # return root for upper level
        return root