#Write up to Hackerrank Designer PDF Viewer
#Challenge : https://www.hackerrank.com/contests/101hack40/challenges/designer-pdf-viewer

h = list(map(int,input().split()))https://www.hackerrank.com/contests/101hack40/challenges/designer-pdf-viewer
s = str(input())

width = 0
height = 0

for c in s:
    index = ord(c) - ord('a')
    width += 1
    height = max(height, h[index])
    
print(height*width)