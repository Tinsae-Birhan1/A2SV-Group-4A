from collections import defaultdict

graph = defaultdict(list)
n=int(input())
source = []
sinks = []
sets = set()
removed = set()
for i in range(n):
    row = list(map(int, input().split()))
    if 1  not in row:
        source.append(i+1)
    

    for j in range(len(row)):
        if row[j] != 1 and j+1 not in removed:
            sets.add(j+1)
        elif row[j] == 1 and j+1 in sets:
            sets.remove(j+1)
            removed.add(j+1)

    

print(len(sets), *list(sets))
print(len(source), *source)