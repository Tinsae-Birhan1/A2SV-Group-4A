class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output=[]
        for i, j in enumerate(l):
            x=True
            sub=nums[j:r[i]+1]
            sub.sort()
            diff=sub[0]-sub[1]
            for i in range(1, len(sub)-1):
                if sub[i]-sub[i+1]!=diff:
                    x=False
                    break
            output.append(x)
        return output