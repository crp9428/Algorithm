import sys
input = sys.stdin.readline
print = sys.stdout.write

a, b = map(lambda x: x[::-1], input().strip().split())
aLen, bLen = len(a), len(b)
maxLen = max(aLen, bLen)
q, x, y, sumAB = 0, 0, 0, ""

for i in range(maxLen):
    x = int(a[i]) if i < aLen else 0
    y = int(b[i]) if i < bLen else 0
    tSum = (x + y + q)
    q = tSum // 10
    sumAB += str(tSum % 10)
    
if q != 0:
    sumAB += str(q)

result = int(sumAB[::-1])
print(f"{result}")