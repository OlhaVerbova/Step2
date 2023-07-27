from pathlib import Path
import file_processing
list_images = []
list_video = []
list_audio = []
list_archives = []
list_documents = []
list_unknown_exeptions = []
known_exeptions = []
unknown_exeptions = []

def list_files_in_a_category(path_to_folder: str):
    path = Path(path_to_folder)    

    for item in path.glob('**/*'):
        
        item_suffix = item.suffix.split('.')
        if item.is_file() and (item_suffix[-1].upper() in file_processing.IMAGES):
            list_images.append(item.name)
            if item_suffix[-1].upper() not in known_exeptions:
                known_exeptions.append(item_suffix[-1].upper())
        elif item.is_file() and (item_suffix[-1].upper() in file_processing.AUDIO):
            list_audio.append(item.name)
            if item_suffix[-1].upper() not in known_exeptions:
                known_exeptions.append(item_suffix[-1].upper())
        elif item.is_file() and (item_suffix[-1].upper() in file_processing.VIDEO):
            list_video.append(item.name)
            if item_suffix[-1].upper() not in known_exeptions:
                known_exeptions.append(item_suffix[-1].upper())
        elif item.is_file() and (item_suffix[-1].upper() in file_processing.DOCUMENTS):
            list_documents.append(item.name)
            if item_suffix[-1].upper() not in known_exeptions:
                known_exeptions.append(item_suffix[-1].upper())
        elif item.is_file() and (item_suffix[-1].upper() in file_processing.ARCHIVES):
            list_archives.append(item.name)
            if item_suffix[-1].upper() not in known_exeptions:
                known_exeptions.append(item_suffix[-1].upper())
        else:
            list_unknown_exeptions.append(item.name)
            if item_suffix[-1].upper() not in unknown_exeptions:
                unknown_exeptions.append(item_suffix[-1].upper())         
   
        
        

def print_lists(path_to_folder: str):
    list_files_in_a_category(path_to_folder)
    print(f"Изображения: {list_images}")
    print(f"Видео: {list_video}")
    print(f"Аудио: {list_audio}")
    print(f"Документы {list_documents}")
    print(f"Архивы: {list_archives}")
    print(f"Прочее {list_unknown_exeptions}")
    print(f"Известные расширения: {known_exeptions}")
    print(f"Неизвестные расширения: {unknown_exeptions}")

p = "C:\\Users\\verbo\\Documents\\Python\\Go IT\\6 home work\\Мусор"
list_files_in_a_category(p)
print_lists(p)









