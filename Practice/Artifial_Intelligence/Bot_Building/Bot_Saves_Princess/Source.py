import sys
N = int(input())
BotX = -1; BotY = -1; PeachX = -1; PeachY = -1
for i in range(N):
    s = str(input().strip())
    peach = s.find("p")
    bot = s.find("m")
    if peach != -1:
        PeachX = peach
        PeachY = i
    if bot != -1:
    	BotX = bot
    	BotY = i

while BotX != PeachX and BotY != PeachY:
	print("BotX = {}, BotY = {}, PeachX = {}, PeachY = {}".format(BotX,BotY,PeachX,PeachY),file=sys.stderr)
	if BotY > PeachY:
		BotY -= 1
		print("UP")
	if BotY < PeachY:
		BotY += 1
		print("DOWN")
	if BotX > PeachX:
		BotX -= 1
		print("LEFT")
	if BotX < PeachX:
		BotX += 1
		print("RIGHT")