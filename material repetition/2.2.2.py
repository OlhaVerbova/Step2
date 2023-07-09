def return_more_sum(list_num):
    result = 0
    num_list = []
    num_list = list_num.split()
    result_list = [int(num) for num in num_list]
    

    for i in range(len(result_list) - 1):
        
        if result_list[i + 1] > result_list[i]:
            
            result += 1

    return result

text = input()
print(return_more_sum(text))