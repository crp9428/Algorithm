from collections import deque

def solution(arr):
    arr, answer = deque(arr), []
    while arr:
        n = arr.popleft()
        if not answer or answer[-1] != n:
            answer.append(n)
    
    return answer