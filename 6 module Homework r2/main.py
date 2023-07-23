from make_new_dir import make_new_dir
from normolize import normalize
from parsing_the_folder import parsing_the_folder
from delete_empty import delete_empty_folder
def main():
    p = "C:\\Users\\verbo\\Documents\\Python\\Go IT\\6 home work\\Мусор"
    make_new_dir(p)
    parsing_the_folder(p)
    delete_empty_folder(p)

if __name__ == "__main__":
    main()