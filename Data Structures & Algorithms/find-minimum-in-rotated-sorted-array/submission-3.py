class Solution:
    def findMin(self, nums: List[int]) -> int:
        # # Approach 1: One Pass (Trivial) - O(n)
        # # Input = list of ints
        # # Output = minimum number

        # minimum = 9999999999999
        # for i in nums:
        #     minimum = min(i, minimum)

        # return minimum

        # Approach 2: binary search - O(logn)
        # minimum is the only place where the right value is smaller than the left
        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums)-1
        minimum = 0
        while l <= r:
            # evaluate middle number against number on its left
            m = (l + r) // 2
            # print(m, nums[m], "|", l, nums[l], "|", r, nums[r])
            if nums[m] < nums[m-1]:
                return nums[m]
            elif nums[r] < nums[m]:
                # number in right half
                l = m + 1
            else:
                r = m

        return -1
