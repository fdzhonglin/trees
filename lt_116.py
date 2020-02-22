
from collections import deque

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.dfs(root)
        #self.bfs(root)
        
        return root
    
    # dfs is tricky
    # here is an pefect binary tree
    #            1
    #       2        3
    #     4   5     6  7
    #
    #  you can easyly find out that in pre order area you can connect left child and right child
    # however, how to connect 5 to 6 need an aha moment. Since you know the next of 2
    # is 3, then for the right child of 2 need to connect to left node of 3.
    # To be honest, I don't think I can bring this solution if I don't know the answer first
    
    def dfs(self, root):
        # stop condition
        if root is None:
            return 
        
        if root.left is not None:
            root.left.next = root.right
            
            if root.next is not None:
                # this part is tricky, you need to think hard to find this solution
                root.right.next = root.next.left
        
        # skeleton: go left and right
        self.dfs(root.left)
        self.dfs(root.right)
        
        return
    
    # bfs solution is easy
    # just traverse the tree level by leve
    # for each level connect the nodes one by one
    def bfs(self, root):
        if root is None:
            return
        
        # skeleton for bfs: Init bfs queue
        q = deque()
        q.append(root)
        
        # skeleton for bfs: stop when q is empty
        while len(q):
            # operation for this specific question
            prev_node = None
            
            # skeleton for bfs:
            node_count = len(q)
            for i in range(node_count):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                # skeleton end :)
                
                # connect node in same level one by one
                if prev_node != None:
                    prev_node.next = node
                prev_node = node 
            