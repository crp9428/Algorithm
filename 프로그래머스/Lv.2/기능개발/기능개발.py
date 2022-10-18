from collections import deque
def solution(progresses, speeds):
    progresses, speeds = deque(progresses), deque(speeds)
    answer, count = [], 0
    while progresses:
        for i in range(len(progresses)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
        
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        
        if count > 0:
            answer.append(count)
            count = 0
    
    return answer