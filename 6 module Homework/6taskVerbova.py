# Переименовать папку
"""rename = normalize(item.name)
            result_name = item.with_name(rename)
            item.rename(result_name)"""
#Переименовать файл 
"""rename = normalize(item.stem) + item.suffix
            result_name = item.with_name(rename)
            item.rename(result_name)"""
from pathlib import Path

def normalize(text: str)-> str:
    
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}  
    
    mini_cy = tuple(CYRILLIC_SYMBOLS)
    for c, l in zip(mini_cy, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    return text.translate(TRANS)


def parsing_the_folder(path_to_folder: str):
    # Словарь для сохранения всех типов файлов
    data_dictionary = {}    
    path = Path(path_to_folder)
     
    """"for i in path.iterdir():
        if i.suffix == None:
            parsing_the_folder(path_to_folder)
        else:
            for j in path.iterdir():
                print(j.name)"""  

    for item in path.iterdir():
        if item.is_file():            
            print("Тут есть файл: ", item.name)
        elif item.is_dir():            
            print("Тут есть папка: ", item.name)
            parsing_the_folder(item)
def make_new_dir(path_to_folder: str):
    path = Path(path_to_folder)
    images_flag = None
    documents_flag = None
    audio_flag = None
    video_flag = None
    archives_flag = None

    for item in path.iterdir():
        if item.is_dir():            
            if item.name == "images":
                images_flag = False
                break
            else:
                images_flag = True
    for item in path.iterdir():
        if item.is_dir():            
            if item.name == "documents":
                documents_flag = False
                break
            else:
                documents_flag = True
    for item in path.iterdir():
        if item.is_dir():            
            if item.name == "audio":
                audio_flag = False
                break
            else:
                audio_flag = True
    for item in path.iterdir():
        if item.is_dir():            
            if item.name == "video":
                video_flag = False
                break
            else:
                video_flag = True
    for item in path.iterdir():
        if item.is_dir():            
            if item.name == "archives":
                archives_flag = False
                break
            else:
                archives_flag = True

    if images_flag:
        images_folder = path.joinpath("images")
        images_folder.mkdir()
    if documents_flag:
        images_folder = path.joinpath("documents")
        images_folder.mkdir()
    if audio_flag:
        images_folder = path.joinpath("audio")
        images_folder.mkdir()
    if video_flag:
        images_folder = path.joinpath("video")
        images_folder.mkdir()
    if archives_flag:
        images_folder = path.joinpath("archives")
        images_folder.mkdir()
    
def main():
    p = "C:\\Users\\verbo\\Documents\\Python\\Go IT\\6 home work\\Мусор"
    make_new_dir(p)
    parsing_the_folder(p)
if __name__ == "__main__":
    main()