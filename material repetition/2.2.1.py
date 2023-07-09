def return_num_points(num):
    first = 0
    second = 0
    third = 0
    fought = 0
    
    while num != 0:        
        n = input( )
        k_old = []
        k_old.append(n)
        k_temp = k_old[0].split() 
        k = [int(num) for num in k_temp]  

        if k[0] > 0 and k[1] > 0:
            first += 1
        elif k[0] < 0 and k[1] > 0:
            second += 1
        elif k[0] < 0 and k[1] < 0:
            third += 1
        elif k[0] > 0 and k[1] < 0:
            fought += 1
        num -= 1
    
    print(f"Первая четверть: {int(first)}\nВторая четверть: {second}\nТретья четверть: {third}\nЧетвертая четверть: {fought}")


num = int(input("Enter number of try: "))
return_num_points(num)