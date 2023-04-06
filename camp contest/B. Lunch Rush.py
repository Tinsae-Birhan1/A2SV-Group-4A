n, k = map(int, input().split())

max_joy = float("-inf")

for i in range(n):
    f, t = map(int, input().split())
    if t > k:
        joy = f - (t - k)
    else:
        joy = f
    max_joy = max(max_joy, joy)

print(max_joy)
