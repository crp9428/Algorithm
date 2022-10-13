import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().strip())
for i in range(n):
    for j in range(n - (i + 1)):
        print(" ")
    for k in range(i + 1):
        print("*")
    print("\n")