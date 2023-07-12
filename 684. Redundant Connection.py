class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
            # num of nodes
        n = len(edges)
 
        # node: parent
        parent = [i for i in range( n+1)]
 
        # size of unions
        size = [1 for i in range( n+1)]
 
 
        def union(a, b):
            # Join a and b
            a = find(a)
            b = find(b)
 
            if a == b:
                return False
 
            if size[a] > size[b]:
                parent[b] = a
                size[a] += size[b]
 
            else:
                parent[a] = b
                size[b] += size[a]
 
            return True
 
 
        def find(a):
            # finds the representative of a
            while parent[a] != a:
                a = parent[a]
 
            return a
 
 
        ans = None
        for a,b in edges:
            connected = union(a,b)
 
            if not connected:
                ans = [a,b]
 
        return ans
    
    
        