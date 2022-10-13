import sys
input = sys.stdin.readline
print = sys.stdout.write

N = input().strip()
n = int(N)
N = N.zfill(2)
sum = int(N[0]) + int(N[1])
ab = N[-1:] + str(sum)[-1:]
cnt = 1

while(n != int(ab)):
    sum = int(ab[0]) + int(ab[1])
    ab = ab[-1:] + str(sum)[-1:]
    cnt += 1
print("%d\n" % cnt)