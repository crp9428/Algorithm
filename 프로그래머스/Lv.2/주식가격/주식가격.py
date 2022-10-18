def solution(prices):
    answer, stack = [0], [len(prices) - 1];
    for i in range(len(prices) - 2, -1, -1):
        if prices[i] > prices[stack[-1]]:
            stack.append(i)
        else:
            while stack and prices[i] <= prices[stack[-1]]:
                stack.pop()
            stack.append(i)
        
        if len(stack) >= 2:
            answer.append(stack[-2] - stack[-1])
        else:
            answer.append(len(prices) - 1 - stack[-1])
    
    answer.reverse()
    return answer