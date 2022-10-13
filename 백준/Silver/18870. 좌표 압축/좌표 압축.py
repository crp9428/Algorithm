import sys
input = sys.stdin.readline
print = sys.stdout.write

n, origin = int(input().strip()), list(map(int, input().strip().split()))
s, dic = sorted(list(set(origin))), dict()

for i, v in enumerate(s):
    dic[v] = i

for i in range(n):
    origin[i] = str(dic[origin[i]])

print(" ".join(origin))