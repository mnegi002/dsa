class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i , j = 0 , 1 
        while j< n :
            if nums[j]!= nums[i]:
                nums[i+1] = nums[j]
                i+=1
            j+=1
            
        return i + 1
