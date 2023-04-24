class Solution:
    def isPalindrome(self, s: str) -> bool:
        count=""
        for i in s:
            if i.isdigit() or i.isalpha():
                count += i
        count = count.lower()
        l= 0 
        r = len(count)-1
        while r>l:
            if count[l] != count[r]:
                return False
            l+=1
            r-=1
        return True
