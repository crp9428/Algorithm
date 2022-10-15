import sys
input = sys.stdin.readline

N = int(input().strip())
def main():
    if N == 1:
        print(1)
        return
    elif N == 2:
        print(2)
        return
    
    a = 1; b = 2; sum = 0
    for i in range(3, N + 1):
        sum = (a + b) % 15746
        a = b
        b = sum
    print(sum)

main()