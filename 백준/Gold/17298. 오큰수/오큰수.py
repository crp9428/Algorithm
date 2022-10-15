import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
A = list(map(int, input().strip().split()))

stack, answer = [], [-1 for _ in range(N)]
for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

for v in answer:
    print("%d " % v)