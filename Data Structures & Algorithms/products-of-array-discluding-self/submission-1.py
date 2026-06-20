class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input: list of numbers
        # output: list of products (excl nums[i])

        ret_list = []

        # # Approach 1: Brute Force
        # for i in range(len(nums)):
        #     curr_product = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         curr_product *= nums[j]
        #     ret_list.append(curr_product)

        # return ret_list

        # Approach 2: One Pass?
        zeros = 0
        full_product = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                full_product *= nums[i]
            else:
                zeros += 1

        if zeros > 1: return [0] * len(nums)

        # case where there is one zero or no zeros
        for i in range(len(nums)):
            if nums[i] == 0:                                              
                ret_list.append(full_product)
            elif nums[i] != 0 and zeros == 1:
                ret_list.append(0)
            else:
                ret_list.append(full_product//nums[i])

        return ret_list