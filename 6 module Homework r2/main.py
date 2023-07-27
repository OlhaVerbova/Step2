from make_new_dir import make_new_dir
from parsing_the_folder import parsing_the_folder
from delete_empty import delete_empty_folder
from rename_files_folders import rename_all_folders_files
from unpacking_archives import unpack_archives
from file_list_in_a_category import print_lists

def main():
    p = "C:\\Users\\verbo\\Documents\\Python\\Go IT\\6 home work\\Мусор"
    make_new_dir(p) #Создаем папку
    parsing_the_folder(p) #Итерируем папки
    delete_empty_folder(p) #Удаляем пустые папки    
    rename_all_folders_files(p) #Переименовываем папки
    unpack_archives() # распаковка архива
    print_lists(p)
    #rename_all_folders_files(p) #Переименовываем папки
    
    

if __name__ == "__main__":
    main()