import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
cards = list(0 for _ in range(20000001))
for n in list(map(int, input().strip().split())):
    cards[n] += 1

M = int(input().strip())
for q in list(map(int, input().strip().split())):
    print("%d " % cards[q])