class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprof = 0 
        mini = prices[0]
        for i in range (n):
            mini = min(prices[i] , mini)
            diff = prices[i] - mini 
            maxprof = max(maxprof, diff)
        return maxprof