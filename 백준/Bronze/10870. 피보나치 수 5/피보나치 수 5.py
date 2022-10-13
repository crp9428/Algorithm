import sys
input = sys.stdin.readline

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("%d" % (fibonacci(int(input().strip()))))
    