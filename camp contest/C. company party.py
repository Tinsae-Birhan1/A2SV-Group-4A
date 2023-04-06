n = int(input())

managers = [-1] + [int(input()) for _ in range(n)]


# Count the number of employees without a manager
no_managers = managers.count(-1)

# Create an adjacency list to represent the company hierarchy
adj_list = [[] for _ in range(n)]

for i, manager in enumerate(managers):
    if manager != -1:
        adj_list[manager - 1].append(i)

# Perform a DFS on the company hierarchy to find the maximum depth
max_depth = 0

def dfs(node, depth):
    global max_depth
    max_depth = max(max_depth, depth)
    for child in adj_list[node]:
        dfs(child, depth + 1)

for i in range(n):
    if managers[i] == -1:
        dfs(i, 1)

# The minimum number of groups is the maximum depth + the number of employees without a manager
print( no_managers)
