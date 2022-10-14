import sys
input = sys.stdin.readline
print = sys.stdout.write

coorX, coorY = list(), list(), 
for x, y in list(map(int, input().strip().split()) for _ in range(3)):
    coorX.append(x)
    coorY.append(y)

x = coorX[2] if coorX[0] == coorX[1] else coorX[1] if coorX[0] == coorX[2] else coorX[0]
y = coorY[2] if coorY[0] == coorY[1] else coorY[1] if coorY[0] == coorY[2] else coorY[0]
print("%d %d" % (x, y))