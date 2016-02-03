def pgcd(a,b):
    if a % b == 0:  return b
    else: return pgcd(b, a % b)

def isGhost(a,b,c,d):
    cond1 = ((a - b)% 3) == 0
    cond2 = ((b + c)%5) == 0
    cond3 = ((a*c)%4) == 0
    cond4 = pgcd(a,d) == 1
    return cond1 and cond2 and cond3 and cond4


A,B,C,D = list(map(int,input().strip().split(' ')))
res = 0
for a in range(1,A+1):
    for b in range(1,B+1):
        for c in range(1,C+1):
            for d in range(1,D+1):
                if isGhost(a,b,c,d):
                    res += 1
print(res)