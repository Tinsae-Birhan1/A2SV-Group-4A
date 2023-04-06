    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        if n == 1:
            print(1)
            print(1)
            print(1)
            print()
            continue
        b = [True] * (n+1)
        b[0] = False
        for i in a:
            b[i] = False
        print(b.count(True))
        for idx, i in enumerate(b):
            c = []
            if i == True:
                t = idx
                while a[t-1] != -1 and a[t-1] != t:
                    c.append(t)
                    x = t
                    t = a[t-1]
                    a[x-1] = -1
                if a[t-1] != -1:
                    c.append(t)
                    a[t-1] = -1
                c.reverse()
                print(len(c))
                print(*c)
                
        print()