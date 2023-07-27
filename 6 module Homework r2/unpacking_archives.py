import shutil
from pathlib import Path
import make_new_dir

def unpack_archives():
    path = Path(make_new_dir.path_archives)
    for item in path.iterdir():
        if item.is_file():
            folred_for_archive = make_new_dir.path_archives / item.stem
            folred_for_archive.mkdir(exist_ok=True)
            shutil.unpack_archive(item, folred_for_archive)
    