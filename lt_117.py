from collections import deque

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.tricky_bfs(root)
        #self.bfs(root)
        
        return root

    # since the node has next pointer, this means you can 
    # access the nodes in the same level with it.
    # therfore, instead use queue to save level nodes. Go with next :)
    # This new tress is like a normal tree but also with list data structure for each level
    def tricky_bfs(self, root):
        # stop condition
        if root is None:
            return 
        
        # just imagine all the nodes in the next level as a list
        # for opereration to add more nodes to list, you need a tail
        # for iteration to the next level, you need a head to access the list
        next_level_head = None
        next_level_tail = None
        
        # iterate nodes in the same level
        current_node = root
        while current_node:
            if current_node.left is not None:
                # put left child into list
                if next_level_tail is not None:
                    next_level_tail.next = current_node.left
                next_level_tail = current_node.left
                
            if current_node.right is not None:
                # put right child into list
                if next_level_tail is not None:
                    next_level_tail.next = current_node.right
                next_level_tail = current_node.right
            
            # first Not None node is the head of next level
            if next_level_head is None:
                if current_node.left is not None:
                    next_level_head = current_node.left 
                else:
                    next_level_head = current_node.right
            
            # write down this line first in case you forget
            current_node = current_node.next
        
        self.tricky_bfs(next_level_head)
        
    
    # same solution as question 116 if you use the BFS solution.  
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
            