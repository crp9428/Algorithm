def solution(s):
    s, answer, c = list(s), True, 0
    while s:
        if s.pop() == ')':
            c += 1
        else:
            if c > 0:
                c -= 1
            else:
                answer = False
                break
    if c > 0:
        answer = False
    
    return answer