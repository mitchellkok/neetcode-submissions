class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input - list on numbers
        # output array of indexes

        # hmap used to store key-val: complement and index
        hmap = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hmap.keys():
                # complement has been stored already
                ret = [i, hmap[comp]]
                ret.sort()
                return ret
            if nums[i] not in hmap.keys():
                # store this to be used as a complement
                hmap[nums[i]] = i
            

        return [-1,-1]