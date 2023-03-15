class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        count= defaultdict(int)
        ans=0
        for r in range(len(s)):
            count[s[r]] += 1
            if (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans , r-l+1)
        return ans


            