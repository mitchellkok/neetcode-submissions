class Solution:
    def climbStairs(self, n: int) -> int:
        # # Approach 1: Recursion
        # # if 1 step, there is one way to go up; if 2 steps, there are 2 ways

        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2

        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # Approach 2: DP, using two storage variables
        # we want to see how many ways to reach the current step from previous and two below
        cur, prev = 1,1 
        for i in range(n):
            # get to current step from previous
            temp = cur # ways to reach current step from previous
            cur = cur + prev
            prev = temp

        return prev
