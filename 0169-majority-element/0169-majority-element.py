class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        # freq = {}
        # for num in nums:
        #     if num in freq:
        #         freq[num]+=1
        #     else:
        #         freq[num] = 1
        # maxi = max(freq , key=freq.get)
        # if freq[maxi] > (n//2):
        #     return maxi
        # return 0
        count = 0 
        el = 0
        for num in nums:
            if count == 0:
                el = num
            if num == el:
                count+=1
            else:
                count-=1
        return el