import sys
input = sys.stdin.readline
print = sys.stdout.write

S, part = input().strip(), set()

for i in range(0, len(S)):
    for j in range(i+1, len(S)+1):
        part.add(S[i:j])

print("%d" % len(part))