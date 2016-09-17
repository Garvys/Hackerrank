#Write-up to Hackerrank Red John is Back
#Challenge : https://www.hackerrank.com/challenges/red-john-is-back

import sys

T = int(input())

memo = dict()

def factorial(i):
	if i in memo:
		return memo[i]
	if i == 1 or i == 0:
		return 1

	res = i * factorial(i-1)
	memo[i] = res
	return res

def getM(N):
	res = 0;
	nb4 = 0
	while nb4*4 <= N:
		res += factorial(N - 3*nb4) / (factorial(nb4) * factorial(N - 3*nb4 - nb4))
		nb4 += 1
	return res

def eratosthene(n):
    """retourne la liste des nombres premiers <= n (crible d'eratosthene)"""
    if n<2:
        return []
    n += 1
    tableau = [False,False] + [True]*(n-2)
    tableau[2::2] = [False]*((n-2)//2 + n%2) # sup. des nb pairs
    premiers = [2] # initialisation de la tableau des nb 1ers (2 est 1er)
    racine = int(n**0.5)
    racine = racine + [1,0][racine%2] # pour que racine soit impair
    for i in range(3, racine+1, 2):
        if tableau[i]:
            # on enregistre le nouveau nb 1er
            premiers.append(i)
            # on élimine i et ses multiples
            tableau[i::i] = [False]*((n-i)//i + int((n-i)%i>0)) 
    for i in range(racine, n, 2):
        if tableau[i]:
            # on enregistre le nouveau nb 1er (pas de multiples à supprimer)
            premiers.append(i)
    return premiers

tab_M = []

for _ in range(T):
	N = int(input())
	M = getM(N)
	tab_M.append(M)
	

premiers = eratosthene(int(max(tab_M)))

for i in range(T):
	print(sum([a <= tab_M[i] for a in premiers]))