class Solution:
    

    def characterReplacement(self, s: str, k: int) -> int:
        # Inputs: s --> string, k --> number of chars I can replace
        # outputs: length of longest substring after k replacements

        # Approach: Find the largest possible substring with k discrepancies for each unique letter
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                # go through all letters and count the number of matching letters
                if s[r] == c:
                    count += 1

                # while the substring size - count exceeds allowed discrepancies
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    # remove from the front until there are k discrepancies left
                    l += 1
                res = max(res, r - l + 1)
        return res
