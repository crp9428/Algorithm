import sys
import math
input = sys.stdin.readline
print = sys.stdout.write

def isPrime(n):
    if n == 1:
        return False
    ii = math.floor(math.sqrt(n)) + 1
    for i in range(2, ii):
        if n % i == 0:
            return False
    return True

N = int(input().strip())
numbers = list(map(int, input().strip().split()))
count = 0
for v in numbers:
    count = count + 1 if isPrime(v) else count + 0

print(f"{count}")

