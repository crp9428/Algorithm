import sys
input = sys.stdin.readline

N = int(input().strip()); 
if N == 1: 
    print(0); exit()
elif N == 2 or N == 3:
    print(1); exit()
    
count = [31 for _ in range(10**6 + 1)]
count[0] = 0; count[1] = 0; count[2] = 1; count[3] = 1

for i in range(4, N + 1):
    if i % 3 == 0:
        count[i] = min(count[i//3], count[i-1]) + 1
    if i % 2 == 0:
        count[i] = min(min(count[i//2], count[i-1]) + 1, count[i])
    count[i] = min(count[i], count[i-1] + 1)

print(count[N])