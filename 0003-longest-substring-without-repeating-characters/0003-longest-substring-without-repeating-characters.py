class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0 
        longest = 0 
        seen = set()
        for i in range(n):
            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
            longest = max(longest, i - left +1 )
        return longest 
            