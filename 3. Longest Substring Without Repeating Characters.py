class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set()
        res = 0
        left = 0
        for right in range(len(s)):
            while s[right] in sets:
                sets.remove(s[left])
                left+=1
            sets.add(s[right])
            res=max(res, right-left+1)
        return res