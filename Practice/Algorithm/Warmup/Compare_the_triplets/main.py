#Write-up to Hackerrant Compa teh triplets
#Challenge : https://www.hackerrank.com/challenges/compare-the-triplets

A = list(map(int,input().split()))
B = list(map(int,input().split()))

resA = 0
resB = 0

for i in range(len(A)):
	resA += A[i] > B[i]
	resB += B[i] > A[i]

print('{} {}'.format(resA, resB))