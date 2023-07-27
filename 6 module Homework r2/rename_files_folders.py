from pathlib import Path
from normolize import normalize
def rename_all_folders_files(path_to_folder: str):
    path = Path(path_to_folder)
    for item in path.iterdir():
        if item.is_file(): 
            rename = normalize(item.stem) + item.suffix
            result_name = item.with_name(rename)
            item.rename(result_name)
        
        elif item.is_dir():
            rename = normalize(item.name)
            result_name = item.with_name(rename)
            item.rename(result_name) 

            rename_all_folders_files(item)

def rename_all_files(path_to_folder: str):
    path = Path(path_to_folder)
    for item in path.iterdir():
        if item.is_file(): 
            rename = normalize(item.stem) + item.suffix
            result_name = item.with_name(rename)
            item.rename(result_name)
        
        elif item.is_dir():           

            rename_all_folders_files(item)

def rename_all_folders(path_to_folder: str):
    path = Path(path_to_folder)
    for item in path.iterdir():
        if item.is_file():
             continue
        
        elif item.is_dir():
            rename = normalize(item.name)
            result_name = item.with_name(rename)
            item.rename(result_name) 

            rename_all_folders_files(item)

    