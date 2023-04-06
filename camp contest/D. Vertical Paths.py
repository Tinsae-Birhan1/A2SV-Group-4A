def dfs(v):
    if not children[v]:
        return [[v]]
    paths = []
    for child in children[v]:
        for path in dfs(child):
            paths.append([v] + path)
    return paths

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    children = [[] for _ in range(n+1)]
    for i in range(1, n):
        children[p[i]].append(i+1)
    paths = dfs(1)
    print(len(paths))
    for path in paths:
        print(len(path))
        print(*path)
