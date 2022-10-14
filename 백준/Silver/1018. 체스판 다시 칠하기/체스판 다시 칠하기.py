import sys
input = sys.stdin.readline
print = sys.stdout.write

def getCount(board):
    startB = 0; startW = 0
    for i in range(8):
        for j in range(8):
            isEven = (i + j) % 2 == 0
            if isEven:
                if board[i][j] == 'W':
                    startB += 1
                elif board[i][j] == 'B':
                    startW += 1
            else:
                if board[i][j] == 'W':
                    startW += 1
                elif board[i][j] == 'B':
                    startB += 1
    return min(startB, startW)

N, M = map(int, input().strip().split())
origin = list(input().strip() for _ in range(N))

N -= 7; M -= 7
minimum = sys.maxsize
for n in range(N):
    for m in range(M):
        board = origin[n : n + 8]
        for i in range(8):
            board[i] = board[i][m : m + 8]
        count = getCount(board)
        minimum = min(count, minimum)

print(f"{minimum}")