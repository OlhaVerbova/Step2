from pathlib import Path
def parsing_the_folder(path_to_folder: str):
    # Словарь для сохранения всех типов файлов
    data_dictionary = {}    
    path = Path(path_to_folder)
    
    for item in path.iterdir():
        if item.is_file():            
            print("Тут есть файл: ", item.name)
        elif item.is_dir():            
            print("Тут есть папка: ", item.name)
            parsing_the_folder(item)