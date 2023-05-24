class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        d=[[0 for j in range(n)] for i in range(m)]
        visited=[[0 for j in range(n)] for i in range(m)]
        def inbound (row, col):
            return  0 <= row<m and 0 <= col<n
        q=deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    visited[i][j]=1
                    q.append([i,j,0])
        while len(q)>0:
            a,b,dis=q.popleft()
            for r,c in [(a,b-1),(a,b+1),(a-1,b),(a+1,b)]:
                if inbound(r,c) and visited[r][c]==0:
                    visited[r][c]=1
                    d[r][c]=dis+1
                    q.append([r,c,d[r][c]])
        return d
