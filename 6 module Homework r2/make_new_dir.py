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
        global path_images 
        path_images = images_folder.absolute()     
    if documents_flag:
        documents_folder = path.joinpath("documents")
        documents_folder.mkdir()
        global path_documents 
        path_documents = documents_folder.absolute()
    if audio_flag:
        audio_folder = path.joinpath("audio")
        audio_folder.mkdir()
        global path_audio 
        path_audio = audio_folder.absolute()
    if video_flag:
        video_folder = path.joinpath("video")
        video_folder.mkdir()
        global path_video 
        path_video = video_folder.absolute()
    if archives_flag:
        archives_folder = path.joinpath("archives")
        archives_folder.mkdir()
        global path_archives 
        path_archives = archives_folder.absolute()
    