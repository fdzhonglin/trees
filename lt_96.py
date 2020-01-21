
# This question is similar to Question 95, however, simpler.
# Step 1: Use example to get inforamtion
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
# Step 2: Generate the pattern for root
#     * all numbers can be root
#     * After the root is selected, it will divide number into left and right part
#
# Step 3: Same as question 95


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # corner case: don't handle in helper function. 
        # Make more sense here.
        if n == 0:
            return 0
            
        return self.helper(1, n)

    # return type should be count of unique trees that can be build between start and end
    def helper(self, start, end):
        # patter here
        if start > end: 
            return 1 

        count = 0 
        # end + 1 because range function is exclusive on stop
        for i in range(start, end+1):
            # pattern here
            l_count = self.helper(start, i - 1)
            r_count = self.helper(i + 1, end)

            count += l_count * r_count
        
        return count 


# Step 4: Optimize the solution
#   Solution from step 3 will time exceeded with bigger number like 20 which is pretty small.
#   There is one tricky condition hard to find. However, if you think hard on signature of function
#   numTrees(self, n), the argument `n` can be interpreted as how many unique numbers, not from 1 to n.
#   The reason is [1, 2, 3] is no different on [101, 102, 103], as long as it's 3 numbers, you can create
#   5 unique trees.
#   With this information, it mean we can change the signature of helper to helper(self, n).
#   To speedup, we should add diction to save the computed number
#   Therefore change helper(self, n) to helper(self, n, cache)


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # corner case: totally depends on definition. I think 1 is more reasonable then 0 :)
        if n == 0:
            return 0
            
        cache = {}
        return self.helper(n, cache)

    # return type should be count of unique trees that can be build between start and end
    def helper(self, n, cache):
        # patter here
        # This condition is tricky, because the even the child has no numbers, 
        # it should be consider as TreeNode with value None, it make sense to return 1
        if n == 0: 
            return 1
        if n == 1: 
            return 1 

        if n in cache:
            return cache[n]

        count = 0 
        for i in range(n):
            # pattern here
            # left has i numbers, i start from 0
            l_count = self.helper(i, cache)
            # right need exclude root, so - 1
            r_count = self.helper(n - i - 1, cache)

            count += l_count * r_count
        
        cache[n] = count
        return count 
