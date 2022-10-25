import sys
nums = sorted(list(map(int, sys.stdin.readlines())))
print("%d\n%d" % (int(sum(nums)/5), nums[2]))