import math
def string_cost(text):
    one_char_cost = 0.6
    sum_cost = None    

    sum_cost = len(text) * one_char_cost
        
    whole = int(sum_cost)
    if (sum_cost - whole) == 0:
        coins = 0
    else:
        coins = math.ceil(int((sum_cost - whole) * 100)/10)*10

    print(f"{whole} р. {coins} коп.")

text = input()
string_cost(text)