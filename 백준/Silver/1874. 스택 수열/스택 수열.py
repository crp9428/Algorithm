import sys
input = sys.stdin.readline

def main():
    N = int(input().strip())
    stack, op, pNum = [], [], 1

    for _ in range(N):
        n = int(input().strip())
        for _ in range(pNum, n + 1):
            stack.append(pNum)
            pNum += 1
            op.append("+")
        if len(stack) == 0 or stack[len(stack) - 1] != n:
            print("NO")
            return
        else:
            stack.pop()
            op.append("-")
            
    print("\n".join(op))

main()