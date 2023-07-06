def reverce(num):
    num = str(num)
    result = None
    part1_num = None
    part2_num = None
    flag_num = True
    if len(num) <= 5:
        while flag_num:
            num = int(num)
            if num % 10 == 0:
                num = num //10
            else:
                flag_num = False
            num = str(num)
        result = num[-1:-6:-1]
    else:
        part1_num = num[0]
        part2_num = num[-1:-6:-1]
        result = part1_num + part2_num    

    return result

num = int(input())
print(reverce(num))
