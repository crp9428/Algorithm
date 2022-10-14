import sys
input = sys.stdin.readline
import re

string, stack, isSymmetry = "", [], True
while(True):
    string = input().rstrip()
    if string.find(".") == 0 and len(string) == 1:
        break
    elif string.find(".") == -1:
        continue

    string = re.sub("[^\(\)\[\]]", "", string); stack = []; isSymmetry = True
    for s in string:
        if s == "(":
            stack.append("s")
        elif s == "[":
            stack.append("b")
        elif s == ")":
            if len(stack) == 0 or stack.pop() != "s":
                isSymmetry = False
                break
        elif s == "]":
            if len(stack) == 0 or stack.pop() != "b":
                isSymmetry = False
                break
    isSymmetry = isSymmetry and len(stack) == 0
    print("yes") if isSymmetry else print("no")