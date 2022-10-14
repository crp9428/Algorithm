import sys
input = sys.stdin.readline
print = sys.stdout.write

def getGCD(a, b):
    a, b = max(a, b), min(a, b)
    while(a % b != 0):
        a, b = b, a % b

    return b

T = int(input().strip())
for _ in range(T):
    a, b = map(int, input().strip().split())
    lcm = a * b // getGCD(a, b)
    print("%d\n" % lcm)