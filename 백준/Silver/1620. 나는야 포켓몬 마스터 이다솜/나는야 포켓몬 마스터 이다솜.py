import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().strip().split())
alpabet, number = dict(), dict()
for i in range(1, N+1):
    number[i] = input().strip()
    alpabet[number[i]] = i

for _ in range(M):
    q = input().strip()
    if q.isdigit():
        print("%s\n" % number[int(q)])
    else:
        print("%d\n" % alpabet[q])