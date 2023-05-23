class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # arr = [[] for i in range(n)]
        # visited = set()
        
        # for a, b in edges:
        #     arr[a].append(b)
        #     arr[b].append(a)
        # q = deque()
        # q.append(source)
        # visited.add(source)
        # while q:
        #     node = q.popleft()
        #     if node == destination:
        #         return True
        #     arrs = arr[node]
        #     for i in arrs:
        #         if i not in visited:
        #             q.append(i)
        #             visited.add(i)
        # return False
        visited = set()
        arr = [[] for i in range(n)]
        for a, b in edges:
            arr[a].append(b)
            arr[b].append(a)
        
        def dfs(node):
            if node == destination:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            for i in arr[node]:
                if dfs(i) == True:
                    return True
            return False
        return dfs(source)
            
        


