# from array to build trees
# standard divide and conquer questions
# Since the tree has two parts which are left and right with no overlap,
# finding the way to divide the array it's the key
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # leaf condition
        if len(preorder) == 0:
            return None
        
        # first element in preorder is the root of the tree
        root_val = preorder[0]

        # with index of root_val in inorder array will divide the array into left part and right part
        index = -1
        for i in range(len(inorder)):
            if inorder[i] == root_val:
                index = i
                break
        
        # skeleton: generate left root and right root
        # Caveat: the index is tricky to make right, better to use example to make it right
        #             |
        #            \|/
        # preorder   [3, 9, 20, 15, 7]
        #           
        #                |
        #               \|/
        # inorder    [9, 3, 15, 20, 7]
        left_root = self.buildTree(preorder[1:index + 1], inorder[:index])
        right_root = self.buildTree(preorder[index+1:], inorder[index+1:])
        
        # build tree now
        root = TreeNode(root_val)
        root.left = left_root
        root.right = right_root
        
        # return root for upper level
        return root