a = list(map(int, input().split()))
n = a[0]*a[3]+a[2]*a[1]
m = a[1]*a[3]
def nod(x, y):
    while y != 0:
        x, y = y, x%y
    return(x)
nd = nod(n, m)
print(n // nd, m // nd)