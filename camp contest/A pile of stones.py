n = int(input())
operations = input()

count = 0
for i in operations:
    if i == '+':
        count += 1
    else:
        count -= 1
        if count < 0:
            count = 0

print(count)
