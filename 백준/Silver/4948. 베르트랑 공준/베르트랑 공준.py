import sys
input = sys.stdin.readline
import math

primes = [True for _ in range(123456 * 2 + 1)]
primes[0] = primes[1] = False
for i in range(2, math.ceil(math.sqrt(len(primes))) + 1):
    if primes[i] == False: continue
    for j in range(i + i, len(primes), i):
        primes[j] = False

while(True):
    n = int(input().strip())
    if n == 0: break
    case = primes[n + 1 : 2 * n + 1]
    print(case.count(True))