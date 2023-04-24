class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        mincount=-float("inf")
        for l in range(rows):
            tempsum=0
            for r in range(columns):
                if l+2 <= rows-1 and r+2 <= columns-1:
                    tempsum= grid[l][r]+grid[l][r+1]+grid[l][r+2]+grid[l+1][r+1]+grid[l+2][r]+grid[l+2][r+1]+grid[l+2][r+2]
                mincount=max(tempsum,mincount)
        return mincount
        