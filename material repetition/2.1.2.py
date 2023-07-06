def body_mass_index(weight, height):

    index = weight / (height ** 2)
    area_index = [18.5, 25]

    if index < area_index[0]:
        print("Недостаточная масса")
    elif index >= area_index[0] and index <= area_index[1]:
        print("Оптимальная масса")
    else:
        print("Избыточная масса")
        
weight, height = float(input()), float(input())
body_mass_index(weight, height)