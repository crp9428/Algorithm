import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().strip())
arr = sorted(list(list(map(lambda x: int(x) if x.isdigit() else x, input().strip().split())) for _ in range(n)), key = lambda x: x[0])
for v in arr:
    print(f"{v[0]} {v[1]}\n")