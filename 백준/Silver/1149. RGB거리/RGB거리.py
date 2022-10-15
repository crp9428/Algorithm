import sys
input = sys.stdin.readline

N = int(input().strip())
case = []
for n in range(N):
    case.append(list(map(int, input().strip().split())))

for i in range(1, len(case)):
    case[i][0] += min(case[i-1][1], case[i-1][2])
    case[i][1] += min(case[i-1][0], case[i-1][2])
    case[i][2] += min(case[i-1][0], case[i-1][1])
    
print(min(case[N-1]))