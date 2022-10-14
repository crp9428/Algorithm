import sys
input = sys.stdin.readline
print = sys.stdout.write

def getGCD(a, b):
    a, b = max(a, b), min(a, b)
    while(a % b != 0):
        a, b = b, a % b

    return b

a, b = map(int, input().strip().split())
gcd = getGCD(a, b)
lcm = a * b // gcd
print("%d\n%d" % (gcd, lcm))