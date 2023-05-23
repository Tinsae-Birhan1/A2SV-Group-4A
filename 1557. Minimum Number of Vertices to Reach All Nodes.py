class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        a={i for i,j in edges}
        b={j for i,j in edges}
        return a-b
        