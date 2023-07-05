class Solution:
    def find(self, x, y):
        if x[y] == y:
            return y
        x[y] = self.find(x, x[y])  
        return x[y]
    def union(self, C, x, y):
        x1 = self.find(C, x)
        x2 = self.find(C, y)
        if x1 != x2:
            C[x1] = x2
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        C = list(range(n))
        for i in edges:
            self.union(C, i[0], i[1])
        return self.find(C, source) == self.find(C, destination)





    