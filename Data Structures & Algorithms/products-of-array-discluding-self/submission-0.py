class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input: list of numbers
        # output: list of products (excl nums[i])

        ret_list = []

        # Approach 1: Brute Force

        for i in range(len(nums)):
            curr_product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                curr_product *= nums[j]
            ret_list.append(curr_product)

        return ret_list