import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
cards = dict()
for n in list(map(int, input().strip().split())):
    cards[n] = cards[n] + 1 if n in cards else 1
        
M = int(input().strip())
for q in list(map(int, input().strip().split())):
    print("%d " % cards[q]) if q in cards else print("0 ")