def solution(numbers):
    answer = []

    for i in range(len(numbers)) :
        for j in range(len(numbers)) :
            if i == j :
                pass
            
            else:
                answer.append(numbers[i] + numbers[j])
                
    result = sorted(list(set(answer)))
    
    return result