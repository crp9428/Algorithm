from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N, M = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
ijs = list(list(map(lambda x: int(x)-1, input().strip().split())) for _ in range(M))
presum = [nums[0]]
for i in range(1, N):
    presum.append((nums[i] + presum[i-1]))

for i, j in ijs:
    if i == 0:
        print("%d\n" % presum[j])
    else:
        print("%d\n" % (presum[j] - presum[i-1]))