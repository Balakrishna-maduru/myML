import os

class ReadData:
    #def __init__(self):
    #    print("Data reading started")

    def _get_files_to_read(self, path):
        files_to_read = []
        if os.path.isfile(path):
            return [path]
        else:
            for file in os.scandir(path):
                if os.path.isfile(file):
                    files_to_read.append(str(path)+"/"+str(file.name))
            return files_to_read