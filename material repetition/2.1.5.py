def zodiak(year):
    animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык",
                "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
    index_year = None
    index_year = year % 12
    
    return animals[index_year]

year = int(input())
print(zodiak(year))