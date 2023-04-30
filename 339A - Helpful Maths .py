s = input()
count = [0, 0, 0]  
for c in s:
    if c == '1':
        count[0] += 1
    elif c == '2':
        count[1] += 1
    elif c == '3':
        count[2] += 1
new_s = '+'.join(['1']*count[0] + ['2']*count[1] + ['3']*count[2])
print(new_s)
