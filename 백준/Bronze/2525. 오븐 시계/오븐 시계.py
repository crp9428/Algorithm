import sys
input = sys.stdin.readline
print = sys.stdout.write

A, B = map(int, input().strip().split())
C = int(input().strip())

result = [A, B+C]
if result[1] > 59:
    result[0] += result[1] // 60
    result[1] = result[1] % 60
if result[0] >= 24:
    result[0] -= 24
    
print("%d %d" % (result[0], result[1]))