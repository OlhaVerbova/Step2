def iosif_flaviy(n, k):
    list_num = [i for i in range(1, n + 1)]
    flag_num = True
    temp_k = k - 1
    while flag_num:
        if temp_k >= len(list_num):
            temp_k = temp_k % len(list_num)  # Исправление: используем остаток от деления
        else:
            list_num.pop(temp_k)
            temp_k += k - 1
        if len(list_num) == 1:
            flag_num = False
    return list_num[0]

n, k = int(input()), int(input())
print(iosif_flaviy(n, k))