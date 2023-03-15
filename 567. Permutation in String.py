class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x=""
        i=len(s1)-1
        while i>=0:
            x+=s1[i]
            i-=1
        l=0
        r=len(s1)-1
        while r<len(s2):
            if x in s2[l:r+1] or s1 in s2[l:r+1]:
                return True
            r+=1
            l+=1
        return False
