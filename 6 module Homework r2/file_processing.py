
IMAGES = ['JPEG', 'PNG', 'JPG', 'SVG']
DOCUMENTS = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']
AUDIO = ['MP3', 'OGG', 'WAV', 'AMR']
VIDEO = ['AVI', 'MP4', 'MOV', 'MKV']
ARCHIVES = ['ZIP', 'GZ', 'TAR']
UNKNOWN_EXTENSION = []

def images_processing(file_name: str):
    suffix_name = file_name.split(".")
    if suffix_name[-1].upper() in IMAGES:
        return True
    else:
        return False
def documents_processing(file_name: str):
    suffix_name = file_name.split(".")
    if suffix_name[-1].upper() in DOCUMENTS:
        return True
    else:
        return False
def audio_processing(file_name: str):
    suffix_name = file_name.split(".")
    if suffix_name[-1].upper() in AUDIO:
        return True
    else:
        return False
def video_processing(file_name: str):
    suffix_name = file_name.split(".")
    if suffix_name[-1].upper() in VIDEO:
        return True
    else:
        return False
def archives_processing(file_name: str):
    suffix_name = file_name.split(".")
    if suffix_name[-1].upper() in ARCHIVES:
        return True
    else:
        return False