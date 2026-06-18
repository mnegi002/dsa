class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        mini = float('inf')
        sumi = 0
        left = 0 
        for i in range(n):
            sumi+=nums[i]
            while sumi >=target:
                mini = min(mini , i-left+1)
                sumi -= nums[left]
                left+=1

        return 0 if mini == float('inf') else mini

                

                

            