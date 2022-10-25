from sys import stdin, stdout
input = stdin.readline

N = int(input().strip())
arr = list(list(0 for _ in range(100)) for _ in range(100))

for _ in range(N):
    x, y = map(int, input().strip().split())
    for ix in range(x, x+10):
        for iy in range(y, y+10):
            arr[ix][iy] = 1

area = 0
for i in range(100):
    for j in range(100):
        area += arr[i][j]

print(area)