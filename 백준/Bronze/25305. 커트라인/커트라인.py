import sys
input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().strip().split())
arr = sorted(list(map(int, input().strip().split())), reverse=True)
print(f"{arr[k-1]}")