class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def bfs(a):
            res = []
            for i in range(4):
                d= str((int(a[i]) + 1) % 10)
                res.append(a[:i] + d + a[i + 1 :])
                d = str((int(a[i]) + 10 - 1) % 10)
                res.append(a[:i] + d + a[i + 1 :])
            return res
        q = deque()
        visit = set(deadends)
        q.append(["0000", 0])  
        while q:
            a, b = q.popleft()
            if a == target:
                return b
            for i in bfs(a):
                if i not in visit:
                    visit.add(i)
                    q.append([i, b + 1])
        return -1
