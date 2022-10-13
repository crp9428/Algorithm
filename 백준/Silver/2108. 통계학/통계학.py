import sys
input = sys.stdin.readline
from collections import Counter

n = int(input().strip())
arr = sorted(list(int(input().strip()) for _ in range(n)))

print(round((sum(arr) / n))) # 산술평균
print(arr[n // 2]) # 중앙값

count = Counter(arr).most_common(2)
print(count[0][0]) if n <= 1 else print(count[1][0]) if count[0][1] == count[1][1] else print(count[0][0]) # 최빈값

print(arr[n - 1] - arr[0]) # 범위