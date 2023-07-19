def solution(food_times, k):
    answer = 0
    
    numbers = sorted(food_times.copy())
    
    array_len = len(numbers)
    cnt = 0
    
    for i, num in enumerate(numbers):
        x = num - cnt
        array_len -= i
        
        if(k < array_len or k==0):
            break;
            
        for _ in range(x):
            # print("k = ", k, " - ", array_len)
            k -= array_len
            cnt += 1
            
    
    # print("k=========", k)
    # print("i=========", i)
    result = 0
    count = 0
    
    for idx in range(len(food_times)):
        x = food_times[idx] - i
        if(x<=0): 
            continue
        else:
            if count == k:
                # result = idx
                break;
            count +=1
    answer = idx + 1
    # print(idx+1)
        
    return answer