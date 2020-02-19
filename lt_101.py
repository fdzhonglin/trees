# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# when make decision, need to compare left most and right most node in same lever,
# there is no way for DFS can get two nodes since DFS normally only hold root.
# Therefore, BFS must used for this problem.
from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # BFS need queue to maitain level order
        q = deque()

        # My coding style to append root first
        q.append(root)
        
        while len(q) > 0:
            # standard BFS operation: how many nodes in current level
            nodes_count = len(q)
            
            # Specific for this question: need to save nodes from current level
            current_level_nodes = []
            
            for i in range(nodes_count):
                # standard BFS operation: get node from current level
                node = q.popleft()

                if node != None:
                    # Standard BFS operation: append child to queue which will be the nodes in next level
                    q.append(node.left)
                    q.append(node.right)
                
                # put node into current level
                current_level_nodes.append(node)
                
            
            # compare current level symmetricly to make sure each level is symmetric
            # return only if asymmetric nodes are found
            for i in range(nodes_count/2):
                left_node = current_level_nodes[i]
                right_node = current_level_nodes[nodes_count - 1 - i]
                
                if left_node == None and right_node == None:
                    continue
                    
                if left_node == None or right_node == None:
                    return False
                
                if left_node.val != right_node.val:
                    return False
        
        # No exception means the tree is symmetric
        return True            


        
        
