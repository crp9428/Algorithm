import sys
input = sys.stdin.readline
print = sys.stdout.write
import math

M, N = map(int, input().strip().split())
primes = [True for _ in range(0, N + 1)]
primes[0] = False
primes[1] = False
for i in range(2, math.ceil(math.sqrt(N)) + 1):
    if primes[i] == False: 
        continue
    for j in range(i * 2, N + 1, i):
        primes[j] = False

for i in range(M, N + 1):
    if primes[i]: 
        print("%d\n" % i)