import random
n = int(input())
if n == 0:
    print('')
else:
    a = list(map(int, input().split()))
    def quick(a):
        if len(a) <= 1:
            return a
        else:
            x = random.choice(a)
            l = []
            g = []
            mid = []
            for i in a:
                if i < x:
                    l.append(i)
                elif i > x:
                    g.append(i)
                else:
                    mid.append(i)
            return quick(l) + mid + quick(g)
    ans = (quick(a))
    print(*ans)