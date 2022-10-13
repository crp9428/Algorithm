import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())

# 1. 삽입 정렬
# arr = [int(input().strip())]
# for _ in range(N - 1):
#     num = int(input().strip())
#     for i, v in enumerate(arr):
#         if num < v:
#             arr.insert(i, num)
#             break
#         if i + 1 == len(arr):
#             arr.append(num)
#             break

# for v in arr:
#     print(f"{v}\n")
    
# 2. 버블 정렬
arr = [int(input().strip()) for _ in range(N)]
for i in range(len(arr) - 1, -1, -1):
    for j in range(0, i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

for v in arr:
    print(f"{v}\n")
