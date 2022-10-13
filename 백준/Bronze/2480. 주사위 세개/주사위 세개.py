import sys
input = sys.stdin.readline
print = sys.stdout.write

dice = list(map(int, input().strip().split()))
reward = 0

if dice[0] == dice[1] == dice[2]:
    reward = 10000 + dice[0] * 1000
elif dice[0] == dice[1] or dice[0] == dice[2]:
    reward = 1000 + dice[0] * 100
elif dice[1] == dice[2]:
    reward = 1000 + dice[1] * 100
else:
    reward = max(dice) * 100

print("%d" % reward)