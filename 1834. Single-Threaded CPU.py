class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        res=[]
        heap = []
        cur1 = 0
        cur2 = tasks[0][0]
        while len(res) < len(tasks):
            while (cur1 < len(tasks)) and (tasks[cur1][0] <= cur2):
                heapq.heappush(heap, (tasks[cur1][1], tasks[cur1][2]))
                cur1 += 1
            if heap:
                a, b = heapq.heappop(heap)
                cur2 += a
                res.append(b)
            elif cur1 < len(tasks):
                cur2 = tasks[cur1][0]
        return res
