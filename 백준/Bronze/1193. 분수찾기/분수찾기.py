import sys
input = sys.stdin.readline
print = sys.stdout.write

X = int(input().strip())

num = 0; count = 0
while(X > count):
    num += 1
    count += num

n = 1; d = 1
if(num % 2 == 0):
    n = X - (count - num)
    d = num + 1 - n
else:
    d = X - (count - num)
    n = num + 1 - d

print(f"{n}/{d}")