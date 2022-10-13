import sys
input = sys.stdin.readline
print = sys.stdout.write

tt = int(input().strip())
for t in range(tt):
    kk = int(input().strip())
    nn = int(input().strip())
    arr = [[0]*nn for k in range(kk + 1)]
    for k in range(kk + 1):
        if k == 0:
            for n in range(nn):
                arr[k][n] = 1 if n == 0 else arr[k][n-1] + 1
        else:
            for n in range(nn):
                arr[k][n] = 1 if n == 0 else arr[k - 1][n] + arr[k][n - 1]
    
    print("%d\n" % arr[kk][nn - 1])