class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input: strings s and t
        # output: bool if count of specific letter in s and t match
        # --> Hashmap

        hmap = {}
        
        # iterate through s
        for i in s:
            if i in hmap.keys():
                hmap[i] += 1
            else:
                hmap[i] = 1

        # iterate through t
        for i in t:
            if i in hmap.keys():
                hmap[i] -= 1
                if hmap[i] < 0:
                    return False
            else:
                return False

        # check for remnants
        for key in hmap.keys():
            if hmap[key] != 0:
                return False

        return True