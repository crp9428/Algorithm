import sys
input = sys.stdin.readline

N = int(input().strip())
meetings = [list(map(int, input().strip().split())) for _ in range(N)]

meetings.sort(reverse= True, key= lambda x: (x[0], x[1]))
count = 1; start = meetings[0][0]
for i in range(1, N):
    if start >= meetings[i][1]:
        count += 1
        start = meetings[i][0]
print(count)
