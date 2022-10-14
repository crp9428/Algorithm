import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().strip().split())
notListen, notSee = set([input().strip() for _ in range(N)]), set([input().strip() for _ in range(M)])
notLAS = sorted(list(notListen & notSee))
print("%d\n%s\n" % (len(notLAS), "\n".join(notLAS)))