import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().strip())
have = set(map(int, input().strip().split()))
m = int(input().strip())
cards = list(map(int, input().strip().split()))

for card in cards:
    print('1 ') if card in have else print('0 ')
