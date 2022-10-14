import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
divisors = sorted(list(map(int, input().strip().split())))

print("%d" % (divisors[0]*divisors[-1]))