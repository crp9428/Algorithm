from sys import stdin, stdout
input = stdin.readline
print = stdout.write
import heapq

N = int(input().strip())
heap = []
for x in list(map(int, stdin.readlines())):
    if x != 0:
        heapq.heappush(heap, x)
    elif len(heap) == 0:
        print("0\n")
    else:
        minItem = heapq.heappop(heap)
        print("%d\n" % minItem)