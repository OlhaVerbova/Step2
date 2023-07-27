from pathlib import Path
import make_new_dir
import shutil
from file_processing import images_processing
from file_processing import audio_processing
from file_processing import video_processing
from file_processing import documents_processing
from file_processing import archives_processing

def parsing_the_folder(path_to_folder: str):
    # Словарь для сохранения всех типов файлов
    iterator_of_version_files = 1
    data_dictionary = {}    
    path = Path(path_to_folder)
    
    
    for item in path.iterdir():
        if item.is_file():            
            print("Тут есть файл: ", item.name)
            if images_processing(item.name): # Если название имеет суфикс изображения
                if (path / item.name).exists(): #make_new_dir.path_images 
                    try:
                        new_item_name = item.stem + "_copy_" + str(iterator_of_version_files) + item.suffix
                        result_name = item.with_name(new_item_name) # fix
                        item.rename(result_name) # fix
                        iterator_of_version_files += 1
                        shutil.move(result_name, make_new_dir.path_images)
                        #print(f"Файл {item.name} перемещен в папку {make_new_dir.path_images} 'documents'")
                    except FileNotFoundError:
                        print("от халепа")
                    finally:
                        continue
                else:
                    shutil.move(item, make_new_dir.path_images)
                    print(f"Файл {item.name} перемещен в папку {make_new_dir.path_images.name} 'images'")
            if audio_processing(item.name):
                if (path / item.name).exists():
                    try:
                        new_item_name = item.stem + "_copy_" + str(iterator_of_version_files) + item.suffix
                        result_name = item.with_name(new_item_name) # fix
                        item.rename(result_name) # fix
                        iterator_of_version_files += 1
                        shutil.move(result_name, make_new_dir.path_audio)
                        #print(f"Файл {item.name} перемещен в папку {make_new_dir.path_audio} 'documents'")
                    except FileNotFoundError:
                        print("от халепа")
                    finally:
                        continue
                else:                    
                    shutil.move(item, make_new_dir.path_audio)
                    print(f"Файл {item.name} перемещен в папку {make_new_dir.path_audio.name} 'audio'")
            if video_processing(item.name):
                if (path / item.name).exists():
                    try:
                        new_item_name = item.stem + "_copy_" + str(iterator_of_version_files) + item.suffix
                        result_name = item.with_name(new_item_name) # fix
                        item.rename(result_name) # fix
                        iterator_of_version_files += 1
                        shutil.move(result_name, make_new_dir.path_video)
                        #print(f"Файл {item.name} перемещен в папку {make_new_dir.path_video} 'video'")
                    except FileNotFoundError:
                        print("от халепа")
                    finally:
                        continue
                else:
                    shutil.move(item, make_new_dir.path_video)
                    print(f"Файл {item.name} перемещен в папку {make_new_dir.path_video.name} 'video'")
            if archives_processing(item.name):
                if (path / item.name).exists():
                    try:
                        new_item_name = item.stem + "_copy_" + str(iterator_of_version_files) + item.suffix
                        result_name = item.with_name(new_item_name) # fix
                        item.rename(result_name) # fix
                        iterator_of_version_files += 1
                        shutil.move(result_name, make_new_dir.path_archives)
                        #print(f"Файл {item.name} перемещен в папку {make_new_dir.path_archives} 'archives'")
                    except FileNotFoundError:
                        print("от халепа")
                    finally:
                        continue
                else:
                    shutil.move(item, make_new_dir.path_archives)
                    print(f"Файл {item.name} перемещен в папку {make_new_dir.path_archives.name} 'archives'")
            if documents_processing(item.name):
                if (path / item.name).exists():#есть ли файл в папке
                    try:
                        new_item_name = item.stem + "_copy_" + str(iterator_of_version_files) + item.suffix
                        result_name = item.with_name(new_item_name) # fix
                        item.rename(result_name) # fix
                        iterator_of_version_files += 1
                        shutil.move(result_name, make_new_dir.path_documents)
                        print(f"Файл {item.name} перемещен в папку {make_new_dir.path_documents.name} 'documents'")
                    except FileNotFoundError:
                        print("от халепа")
                    finally:
                        continue                    
                else:
                    shutil.move(item, make_new_dir.path_documents)
                    print(f"Файл {item.name} перемещен в папку {make_new_dir.path_documents.name} 'documents'")
            
        elif item.is_dir():            
            print("Тут есть папка: ", item.name)
            parsing_the_folder(item)

            
