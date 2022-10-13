import sys
input = sys.stdin.readline

print(*sorted(list(input().strip()), reverse=True), sep='')