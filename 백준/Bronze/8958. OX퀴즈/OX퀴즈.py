import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input().strip())
for _ in range(T):
    plus, total = 0, 0
    s = input().strip()
    for c in s:
        if c == "X":
            plus = 0
        else:
            plus += 1
        total += plus
    print("%d\n" % total)