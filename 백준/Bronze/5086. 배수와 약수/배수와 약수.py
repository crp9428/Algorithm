import sys
input = sys.stdin.readline
print = sys.stdout.write

while(True):
    a, b = map(int, input().strip().split())
    if a == b == 0:
        break
    elif a < b and b % a == 0:
        print("factor\n")
    elif a > b and a % b == 0:
        print("multiple\n")
    else:
        print("neither\n")