class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # inputs: s --> String where we want to find longest substring
        # output: int --> length of longest substring

        # Edge case: s is ""
        if len(s) == 0:
            return 0

        maximum = 1

        # Approach: we want to iterate through the string with left and right pointers. 
        # Where there is a duplicate, we can set the left pointer to the second duplicate.
        # Use a hashmap to track duplicates

        l = 0
        r = 1
        hmap = {}
 
        for r in range(len(s)):
            if s[r] in hmap : # duplicate char
                l = max(hmap[s[r]]+1, l) # max to prevent moving to a previous duplicate
            hmap[s[r]] = r  # keep track of index of letter
            cur_count = r - l + 1
            if cur_count > maximum:
                maximum = cur_count

        return maximum


            