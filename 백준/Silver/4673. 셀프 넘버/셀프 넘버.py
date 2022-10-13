import sys
input = sys.stdin.readline
print = sys.stdout.write

def d(n):
    result = n
    while(n > 0):
        result += (n % 10)
        n = n // 10
    return result

length = 10001
arr = list(True for _ in range(length))
arr[0] = False

for i in range(1, length):
    num = d(i)
    if num < length:
        arr[num] = False

for i in range(length):
    if arr[i]:
        print('%d\n' % i)