import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().strip().split()))
sum, sub, mul, div = map(int, input().strip().split())

ops = ['sum' for _ in range(sum)] + ['sub' for _ in range(sub)] + ['mul' for _ in range(mul)] + ['div' for _ in range(div)]
cases = []; visit = [False for _ in range(len(ops))]; arr = ['' for _ in range(len(ops))]

def dfs(depth):
    if depth == len(ops):
        tmp = []
        for v in arr:
            tmp.append(v)
        cases.append(tmp)
        return
    
    for i in range(len(ops)):
        if visit[i]: continue
        visit[i] = True
        arr[depth] = ops[i]
        dfs(depth + 1)
        visit[i] = False

dfs(0)

results = [nums[0] for _ in range(len(cases))]
for i, case in enumerate(cases):
    for j in range(N - 1):
        if case[j] == 'sum':
            results[i] = results[i] + nums[j + 1]
        elif case[j] == 'sub':
            results[i] = results[i] - nums[j + 1]
        elif case[j] == 'mul':
            results[i] = results[i] * nums[j + 1]
        elif case[j] == 'div':
            if results[i] < 0 and nums[j + 1] > 0:
                results[i] = ((results[i] * -1) // nums[j + 1]) * -1
            else:
                results[i] = results[i] // nums[j + 1]

print(max(results))
print(min(results))