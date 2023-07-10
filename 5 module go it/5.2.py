articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

def find_articles(key, letter_case=False):
    flag_case_sensitive = letter_case
    new_list = []
    
    if flag_case_sensitive:
    #Case-sensitive 
        for dictionary in articles_dict:
            title = dictionary['title']
            author = dictionary['author']
            year = str(dictionary['year'])
            if (key in title) or (key in author) or (key in year):
                new_list.append(dictionary)
    else:
    #Not case-sensetive
        
        for dictionary in articles_dict:
            title = dictionary['title']
            author = dictionary['author']
            year = str(dictionary['year'])
            if (key.lower() in title.lower()) or (key.lower() in author.lower()) or (key.lower() in year.lower()):
                new_list.append(dictionary)
    return new_list



text = input("Enter the text: ")
flag_sensetive = False
flag_sensetive = input("Enter smt if you want make search case-sensitive: ")
print(find_articles(text, flag_sensetive))



