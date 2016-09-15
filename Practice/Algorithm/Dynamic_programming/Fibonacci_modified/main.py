#Write up to Hackerrank Fibonacci modified
#Challenge : https://www.hackerrank.com/challenges/fibonacci-modified

t1, t2, n = list(map(int,input().split()))

t = [-1,t1,t2]

for i in range(3, n+1):
    t.append(t[i-2] + t[i-1]*t[i-1])
    
print(t[n])

