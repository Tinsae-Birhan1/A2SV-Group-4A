n = int(input())  
k = int(input())  

adj = [[] for _ in range(n)]

for _ in range(k):
    op, *params = map(int, input().split())

    if op == 1:
        u, v = params
        adj[u - 1].append(v)
        adj[v - 1].append(u)
    elif op == 2:
        u = params[0]
        arr = adj[u - 1]
        print(*arr)


