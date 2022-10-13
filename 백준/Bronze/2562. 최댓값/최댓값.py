import sys
input = sys.stdin.readline
print = sys.stdout.write

maximum, count = 0, 0
for i in range(9):
    num = int(input().strip())
    if num > maximum:
        maximum = num
        count = (i + 1)
print("%d\n%d" % (maximum, count))