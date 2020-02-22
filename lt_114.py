# step 1:
#    From example, I know I must touch all the node to finish the transformation
#    So this is a traversal problem.
# Step 2:
#    The tranformations of left part and right part of any root are independent so
#    normal DFS can solve the problem
# Step 3:
#    From example, we know the list is pre order. for list if we want to do operation quick, we need to return head and tail
#    So left child will return head and tail of left part, right child has the same thing
#    Concatenate node in root with left head, left tail with right head this way we sovle it :)
# Step 4:
#    We need helper since the provided function has no return info

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.transform(root)
        
    def transform(self, root):
        # stop condition: head and tail should be none for null(empty) tree
        if root == None:
            return None, None
        
        # skeleton: return list head and tail from left child and right child
        l_head, l_tail = self.transform(root.left)
        r_head, r_tail = self.transform(root.right)

        # there is no left child on final result, so cut it now
        root.left = None
        
        # we have three lists now. root itself can be considred as single node list
        # l_head, l_tail represent list of left child
        # r_head, r_tail represent list of right child
        # 
        # What need to be done now is connect these three lists :)

        # Start from root, this is the single node list, therefore, head and tail are the same
        head = root
        tail = root
        
        if l_head != None:
            # concatenate list of left child if list of left is not empty
            root.right = l_head
            l_tail.right = r_head
        else:
            # concatenate list of right child anyway
            root.right = r_head
            
        # make tail point to the right node
        if r_tail != None:
            tail = r_tail
        elif l_tail != None:
            tail = l_tail
        
        return head, tail
    
    # head can be removed from implementation, I will leave to you to figure out ^-^
        
        
        