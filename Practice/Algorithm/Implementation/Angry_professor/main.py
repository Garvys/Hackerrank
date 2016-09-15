#Write-up to Hackerrank Anfry Professor
#Challenge : https://www.hackerrank.com/challenges/angry-professor

T = int(input())

for _ in range(T):
	N, K = list(map(int, input().split()))
	a = list(map(int, input().split()))

	if sum([e <= 0 for e in a]) < K:
		print('YES')
	else:
		print('NO')
