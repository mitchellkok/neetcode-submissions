class Solution:
    def isPalindrome(self, s: str) -> bool:
        # left and right pointers
        l = 0
        r = len(s) - 1

        while l < r:
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if l >= r:
                break

            left = s[l].lower()
            right = s[r].lower()
            print(left, right)
            if left != right:
                print(" ", left, right)
                return False
            l += 1
            r -= 1
        
        return True