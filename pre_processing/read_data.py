import os

class ReadData:

    def _get_files_to_read(self, path):
        files_to_read = []
        if path.isfile():
            return [path]
        else:
            for file in os.scandir(path):
                if file.isfile():
                    files_to_read.append(file)
            return files_to_read