#Write-up to Hackerrank Circular Array Rotation
#Challenge : https://www.hackerrank.com/challenges/circular-array-rotation

n, k, q = list(map(int,input().split()))
a = input().split()

for _ in range(q):
	m = int(input())
	print(a[(m - k)%n])