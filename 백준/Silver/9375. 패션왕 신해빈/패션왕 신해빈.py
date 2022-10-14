import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import reduce

T = int(input().strip())
for _ in range(T):
    clothes = dict()
    for _ in range(int(input().strip())):
        name, kind = input().strip().split()
        clothes[kind] = clothes[kind] + 1 if kind in clothes else 1
    count = 1
    for key in clothes.keys():
        count *= (clothes[key]+1)
    print("%d\n" % (count-1))