n, m = map(int, input().split())
num = list(map(int, input().split()))
for k in range(m):
    l, r = map(int, input().split())
    min_val = min(num[l:r + 1])
    found = False 
    for i in range(l, r + 1):
        if num[i] != min_val:
            print(num[i])
            found = True
            break
    if not found:
        print("NOT FOUND")