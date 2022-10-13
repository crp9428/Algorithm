import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import reduce

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
s = input().strip()
result = reduce(lambda acc, cur: acc + str(s.find(cur)) + " ", alphabet, "")
print(result)