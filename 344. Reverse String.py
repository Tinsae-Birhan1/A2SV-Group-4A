class Solution:
    def revString(self, s, left, right):
        if left >= right:
            return 
        s[left], s[right] = s[right], s[left]
        self.revString(s, left+1, right-1)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left =0
        right = len(s) - 1
        return self.revString(s, left, right)
        