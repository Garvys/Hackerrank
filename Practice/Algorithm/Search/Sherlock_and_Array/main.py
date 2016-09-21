#Wrtite up to Hackerranl Sherlock and Array
#Challenge : https://www.hackerrank.com/challenges/sherlock-and-array

T = int(input())

for _ in range(T):
    n = int(input())
    A = list(map(int,input().split()))
    left = 0
    right = sum(A) - A[0]
    
    if len(A) == 1:
        print('YES')
    else:
        found = False
        for i in range(1,len(A)):
            left += A[i-1]
            right -= A[i]
            if left == right:
                found = True
                print('YES')
                break
        if not found:
            print('NO')