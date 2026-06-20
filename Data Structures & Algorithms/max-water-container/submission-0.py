class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # input list of ints (heights)
        # output max amout of water between two heights

        maximum = 0

        # between height indexes i and j, vol is given by (j-i) * min(h[i], h[j])
        # # Approach 1: Brute force - find the volume between any two heights
        # for i in range(len(heights)-1):
        #     for j in range(i+1,len(heights)):
        #         vol = (j-i) * min(heights[i], heights[j])
        #         if vol > maximum:
        #             maximum = vol

        # return maximum

        # Approach 2: Sliding Window
        l = 0
        r = len(heights)-1
        
        while l < r:
            vol = (r-l) * min(heights[r], heights[l])
            if vol > maximum:
                maximum = vol
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return maximum


