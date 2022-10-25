from sys import stdin, stdout
input = stdin.readline

matrix = list(list(map(int, input().strip().split())) for _ in range(9))
row, column, maximum = -1, -1, -1

for r in range(9):
    for c in range(9):
        if matrix[r][c] > maximum:
            maximum = matrix[r][c]
            row = r+1
            column = c+1

print(f'{maximum}\n{row} {column}')