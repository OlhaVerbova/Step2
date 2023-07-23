from pathlib import Path
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
    