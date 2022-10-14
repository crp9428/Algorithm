import sys
input = sys.stdin.readline

N = int(input().strip())
num = 666; count = 1
while(count < N):
    num += 1
    if str(num).find("666") > -1:
        count += 1

print(num)