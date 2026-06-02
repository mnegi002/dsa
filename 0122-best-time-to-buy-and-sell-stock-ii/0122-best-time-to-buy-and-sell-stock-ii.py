class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prof = 0 
        # maxprof = 0
        # mini = prices[0]
        # n = len(prices)
        # for i in range(n):
        #     mini = min(mini, prices[i])
        #     diff = prices[i] - mini 
        #     prof = max(prof , diff)
        #     if prof > 0:
        #         maxprof +=prof
        #         mini = prices[i]
        #         prof = 0 
        # return maxprof

        maxprof = 0 
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxprof+= prices[i] - prices[i-1]

        return maxprof