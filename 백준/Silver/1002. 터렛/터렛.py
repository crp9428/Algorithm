import sys
input = sys.stdin.readline
import math

T = int(input().strip())
result = 0
for tt in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().strip().split())
    distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    if distance == 0 and r1 == r2: # 동심원
        result = -1
    elif distance == r1 + r2: # 외접
        result = 1
    elif distance == abs(r1 - r2): # 내접
        result = 1
    elif abs(r1 - r2) < distance < (r1 + r2): # 두 점에서 만나는 경우
        result = 2
    else: # 만나지 않는 경우
        result = 0
    print(result)