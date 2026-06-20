class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input: list of prices (ints)
        # output: maximum possible profit (int)

        maximum = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = l+1
            if r >= len(prices):
                break
            profit = prices[r] - prices[l]
            if profit > maximum:
                maximum = profit
            r += 1

        return maximum
            

