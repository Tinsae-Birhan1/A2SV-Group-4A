class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i in range(len(equations)):
            u, v = equations[i]
            val = values[i]
            graph[u][u] = graph[v][v] = 1
            graph[u][v] = val
            graph[v][u] = 1 / val
        for k in graph:
            for i in graph:
                for j in graph:
                    if j not in graph[i] and k in graph[i] and j in graph[k]:
                        graph[i][j] = graph[i][k] * graph[k][j]
        res = []
        for query in queries:
            u, v = query
            count = graph[u].get(v, -1)
            res.append(count)

        return res