import sys
input = sys.stdin.readline

N = int(input().strip())
cards = [i for i in range(1, N + 1)]
size, idx = len(cards), 0
while(size > 1):
    idx += 1
    size -= 1
    cards.append(cards[idx])
    idx += 1
print(cards[idx])

