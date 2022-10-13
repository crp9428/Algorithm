import sys

N = int(sys.stdin.readline().strip())
arr = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    arr.append({'x': x, 'y': y, 'n': 0})
    
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if arr[i]['x'] > arr[j]['x'] and arr[i]['y'] > arr[j]['y']:
            arr[j]['n'] += 1
        
for v in arr:
    print(v['n'] + 1, end=" ")