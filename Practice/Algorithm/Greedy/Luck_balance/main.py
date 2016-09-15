#Write up to Hackerrank Luck Balance
#Challenge : https://www.hackerrank.com/challenges/luck-balance

N, K = list(map(int,input().split()))

contests_important = []
contests_unimportant = []
for _ in range(N):
	L, T = list(map(int,input().split()))
	if T == 1:
		contests_important.append(L)
	else:
		contests_unimportant.append(L)

contests_important.sort(reverse=True)

#She loses all the unimportant and loses the important with the much luck involved
res = sum(contests_important[:K]) - sum(contests_important[K:]) + sum(contests_unimportant)

print(res)


