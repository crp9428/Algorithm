import sys
input = sys.stdin.readline
print = sys.stdout.write

sides = [-1, -1, -1]
while(True):
    sides = sorted(list(map(int, input().strip().split())))
    if sides[0] == sides[1] == sides[2] == 0:
        break
    elif sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("right\n")
    else:
        print("wrong\n")