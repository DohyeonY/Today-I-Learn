def solution(arr1, arr2):
    answer = [[] for i in range(len(arr2))]
    
    for i in range(len(arr1)):          
        for j in range(len(arr1[i])):     
            answer[i].append(arr1[i][j] + arr2[i][j])
    
    return answer