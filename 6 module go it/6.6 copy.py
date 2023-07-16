def get_recipe(path, search_id):
    try:
        with open(path, "r") as fh:
            #declare variables
            first_list = []
            second_list = []
            result_dict = []
            while True:
                temp_line = fh.readline()
                if not temp_line:
                    break
                first_list.append(temp_line)
            #delete \n

            for i in range(len(first_list)):
                temp_line = first_list[i].replace("\n", "")
                second_list.append(temp_line)

            #record dictionary

            for i in range(len(second_list)):                
                temp_line = second_list[i].split(",")
                
                recipe_dictionary = {}
                recipe_dictionary["id"] = temp_line[0]
                recipe_dictionary["name"] = temp_line[1]
                ingredients = []
                ingredients.append(temp_line[2])
                ingredients.append(temp_line[3])
                ingredients.append(temp_line[4])
                recipe_dictionary["ingredients"] = ingredients
                result_dict.append(recipe_dictionary)

        resalt_recipes = []
        for dictionary in result_dict:
            if search_id == dictionary["id"]:
                 resalt_recipes.append(dictionary)

        if resalt_recipes:
            return resalt_recipes[0]    
        else:
            return None         

    except FileNotFoundError:
        print("File not found.")
        return 0
path = input("Enter path --> ")
search_id = input("Enter id --> ")
print(get_recipe(path, search_id))
#C:\Users\verbo\Documents\GitHub\Step2\test.txt