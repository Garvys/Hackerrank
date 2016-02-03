#
def nextMove(n,r,c,grid):
    BotX = -1; BotY = -1; PeachX = -1; PeachY = -1
    for i in range(n):
        s = grid[i]
        peach = s.find("p")
        bot = s.find("m")
        if peach != -1:
            PeachX = peach
            PeachY = i
        if bot != -1:
            BotX = bot
            BotY = i
    if BotY > PeachY:
        BotY -= 1
        return "UP"
    if BotY < PeachY:
        BotY += 1
        return "DOWN"
    if BotX > PeachX:
        BotX -= 1
        return "LEFT"
    if BotX < PeachX:
        BotX += 1
        return "RIGHT"
    
    
#Size grid
n = int(input())
# r - row bot
# c - column bot
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
