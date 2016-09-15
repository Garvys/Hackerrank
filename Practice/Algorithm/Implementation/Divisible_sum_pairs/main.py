#Write-up Hackerrank Divisible Sum Pairs
#Challenge : https://www.hackerrank.com/challenges/divisible-sum-pairs

n, k = list(map(int,input().split()))

a = list(map(int,input().split()))

res = 0

for i in range(n):
    for j in range(i+1,n):
        res += ((a[i] + a[j]) % k == 0)

print(res)