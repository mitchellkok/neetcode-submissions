class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Input: list of ints
        # Output: list of list of ints

        ret_list = []

        # Naive solution: 3 nested loops

        # Better solution - 2 pointers
        nums.sort()
        # print(nums)
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                su = nums[i] + nums[l] + nums[r]
                # print(su, nums[i], nums[l], nums[r])
                if su > 0: # needs to be smaller
                    r -= 1
                elif su < 0: # needs to be bigger
                    l += 1
                else:
                    ret_list.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return ret_list