"""n = int(input())
a = list(map(int, input().split()))
ans = []
i = 0
k = n-1 
while i < n :
    weaker = i * a[i] - sum(a[:i])
    stronger = sum(a[i+1:]) - (n-i-1)*a[i]
    ans.append(weaker + stronger)
    i += 1
print(*ans)"""
n = int(input())
a = list(map(int, input().split()))
prefix_sum = [0] * n
prefix_sum[0] = a[0]

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + a[i]

suffix_sum = [0] * n
suffix_sum[n - 1] = a[n - 1]

for i in range(n - 2, -1, -1):
    suffix_sum[i] = suffix_sum[i + 1] + a[i]

ans = []

for i in range(n):
    weaker = i * a[i] - prefix_sum[i]
    stronger = suffix_sum[i] - (n - i - 1) * a[i]
    ans.append(weaker + stronger)

print(*ans)