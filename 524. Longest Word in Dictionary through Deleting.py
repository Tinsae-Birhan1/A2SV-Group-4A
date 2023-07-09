class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans=[]
        
        for i in range(len(dictionary)):
            l=0
            count = True
            while l <len(dictionary[i]):
                if dictionary[i][l] not in s:
                    count = False
                l+=1
            if  count:
                ans.append(dictionary[i])
        res=[]
        lens=0
        for i in range(len(ans)):
            lens=max(lens, len(ans[i]))
        for i in range(len(ans)):
            if len(ans[i])==lens:
                res.append(ans[i])
        if len(res) > 1:
            return min(res)      
        return res[0]
            
