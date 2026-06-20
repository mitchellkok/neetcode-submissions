class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for i in nums:
            if i not in hmap.keys():
                hmap[i] = 1
            else:
                return True

        return False