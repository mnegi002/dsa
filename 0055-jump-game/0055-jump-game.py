class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxi = 0 
        
        for i in range(n):

            if i>maxi:
                return False

            maxi = max(maxi , nums[i]+i)
            if maxi >= n-1:
                return True

        return True
