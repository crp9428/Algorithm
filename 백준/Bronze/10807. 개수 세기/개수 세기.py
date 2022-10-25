from sys import stdin, stdout
from functools import reduce
input = stdin.readline

N = int(input().strip())
nums = list(map(int, input().strip().split()))
v = int(input().strip())
count = reduce(lambda acc, cur: acc + 1 if cur == v else acc + 0, nums, 0)
print(count)