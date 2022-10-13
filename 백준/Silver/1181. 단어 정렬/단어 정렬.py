import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().strip())
arr = sorted(list(set(input().strip() for _ in range(n))), key = lambda x: (len(x), x))
print("\n".join(arr))