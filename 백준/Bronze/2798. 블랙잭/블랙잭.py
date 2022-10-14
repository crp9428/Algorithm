import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
maximum = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            case = arr[i] + arr[j] + arr[k]
            maximum = case if case > maximum and case <= m else maximum

print(f"{maximum}")