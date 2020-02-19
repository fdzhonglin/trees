# BFS for sure, I don't think anyone will ask this question again :)
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BFS need queue to maitain level order
        q = deque()

        # My coding style to append root first
        q.append(root)
        
        # create data structure to hold result
        result = []
        
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
                
                    # put node into current level, according to example, ignore leaf node
                    current_level_nodes.append(node.val)
            
            # append nodes of current level to result
            if len(current_level_nodes) > 0:
                result.append(current_level_nodes)
        
        return result