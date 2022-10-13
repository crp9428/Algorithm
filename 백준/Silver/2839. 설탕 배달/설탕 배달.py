import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
bagArr, max5 = [], N // 5
for i5 in range(0, max5 + 1):
    if (N - i5*5) % 3 == 0:
        bagArr.append((i5 + (N - i5*5) // 3))
        
print(f"{min(bagArr)}") if len(bagArr) > 0 else print("-1")