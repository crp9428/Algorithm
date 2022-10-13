import sys
input = sys.stdin.readline
print = sys.stdout.write
import math

def isPrime(n):
    if n == 1:
        return False
    ii = math.ceil(n / 2) + 1
    for i in range(2, ii):
        if n % i == 0:
            return False
    return True
    
M, N = int(input().strip()), int(input().strip())
arr = [i for i in range(M, N+1) if isPrime(i)]

print("-1") if len(arr) == 0 else print(f"{sum(arr)}\n{min(arr)}\n")