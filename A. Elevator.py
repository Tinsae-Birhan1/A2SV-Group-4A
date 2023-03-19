t = int(input())
for _ in range(t):
    wt, et, ef = map(int, input().split())
    print(min_time(wt, et, ef))