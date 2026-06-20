class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # input: list of numbers
        # output: largest number of consecutive numbers

        if len(nums) == 0:
            return 0

        # initialise return value
        max_consec = 1
        cur_consec = 1

        nums.sort()
        print(nums)
        for i in range(len(nums)-1):
            diff = nums[i+1] - nums[i]
            print(i, nums[i], nums[i+1], diff, cur_consec, max_consec)
            if diff == 1:
                cur_consec += 1
                if cur_consec > max_consec:
                    max_consec = cur_consec
            elif diff > 1:
                cur_consec = 1

        return max_consec