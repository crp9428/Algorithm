import sys
input = sys.stdin.readline

N = int(input().strip())
array, maxNum = [0] * 10001, 0
for _ in range(N):
    num = int(input().strip())
    array[num] += 1
    if maxNum < num:
        maxNum = num

for i in range(0, maxNum + 1):
    if array[i] != 0:
        for j in range(array[i]):
            print(f"{i}")