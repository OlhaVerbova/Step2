from make_new_dir import make_new_dir
from normolize import normalize
from parsing_the_folder import parsing_the_folder
from delete_empty import delete_empty_folder
def main():
    p = "C:\\Users\\verbo\\Documents\\Python\\Go IT\\6 home work\\Мусор"
    make_new_dir(p) #Создаем папку
    parsing_the_folder(p) #Итерируем папки
    delete_empty_folder(p) #Удаляем пустые папки

if __name__ == "__main__":
    main()