#Write up to Hackerrank CamelCase
#Challenge : https://www.hackerrank.com/challenges/camelcase

s = str(input().strip())

nbCapitals = 0
for c in s:
    if ord(c) >= ord('A') and ord(c) <= ord('Z'):
        nbCapitals += 1
        
print(nbCapitals+1)