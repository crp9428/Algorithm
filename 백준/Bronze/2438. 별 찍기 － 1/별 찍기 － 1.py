import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().strip())
for i in range(n):
    for j in range(i + 1):
        print("*")
    print("\n")