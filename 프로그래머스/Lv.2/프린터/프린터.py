import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

def getMaxIdx(arr):
    maxIdx = 0
    for i in range(len(arr)):
        if arr[maxIdx] < arr[i]:
            maxIdx = i
    return maxIdx

def solution(priorities, location):
    answer, priorities = 0, deque(priorities)
    while priorities:
        answer += 1
        maxIdx = getMaxIdx(priorities)
        if maxIdx > 0:
            priorities.rotate(-maxIdx)
            location = location - maxIdx + len(priorities) if location < maxIdx else location - maxIdx
        priorities.popleft()
        location -= 1
        if location == -1:
            break
    
    return answer