class Solution:
    def rob(self, nums: List[int]) -> int:
        # input: list of ints --> money in the ith house
        # output: maximum amount to rob

        # # Approach 1: Brute Force - Recursion
        # # we want to iterate through all houses, finding the possible ways to get there
        
        # # base cases: len(nums) <= 2
        # if len(nums) == 0:
        #     return 0
        # elif len(nums) == 1:
        #     return nums[0] # maximum if 1 number
        # elif len(nums) == 2:
        #     return max(nums[0], nums[1]) # maximum if 2 numbers
        # elif len(nums) == 3:
        #     return max(nums[0]+nums[2], nums[1]) # maximum if 3 numbers

        # consider = []
        # for i in range(2, len(nums)):
        #     # try all possible steps
        #     consider.append(nums[0] + self.rob(nums[i:]))
        
        # for i in range(3, len(nums)):
        #     # try all possible steps
        #     consider.append(nums[1] + self.rob(nums[i:]))

        # return max(consider)

        # # Approach 2: recursion optimised
        # def recurse(i):
        #     # base case: you've reached the end of the line
        #     if i >= len(nums):
        #         return 0
        #     print(nums[i])
        #     maximum = max(recurse(i+1), nums[i] + recurse(i+2))
        #     print("\t",nums[i], maximum)
        #     return maximum

        # return recurse(0)

        # Approach 3: DFS iterative
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # dp[i] will store the max money stolen from the first i houses
        dp = [0] * len(nums)
        
        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Build the solution bottom-up
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            
        return max(dp)