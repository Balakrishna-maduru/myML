import os
import pandas as pd

def get_files_to_read(path, files=[]):
    files_to_read = []
    if len(files) > 0:
        for file in files:
            files_to_read.append(os.path.join(path, file))
    else:
        for file in os.scandir(path):
            if file.is_file():
                files_to_read.append(file)
    return files_to_read