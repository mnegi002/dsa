class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # for i in range(k):
        #     temp = nums[-1]
        #     for j in range(n, 0, -1):
        #         nums[j] = nums[j-1]
        #     nums[0] = temp
        k%=n
        def reverse(left , right):
            while (left<right):
                nums[left], nums[right] = nums[right] , nums[left]
                left+=1 
                right-=1

        reverse(0, n-1)
        reverse(0,k-1)
        reverse(k, n-1)


        