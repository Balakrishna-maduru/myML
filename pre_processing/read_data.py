import os
import pandas as pd

class ReadData:
    #def __init__(self):
    #    print("Data reading started")

    def read(self, path):
        all_data = pd.DataFrame()
        for file in self._get_files_to_read(path):
            df = pd.read_csv(file)
            all_data = pd.concat([all_data, df])

        all_data.columns = all_data.columns.str.upper()
        return all_data

    def _get_files_to_read(self, path):
        files_to_read = []
        if os.path.isfile(path):
            return [path]
        else:
            for file in os.scandir(path):
                if os.path.isfile(file):
                    files_to_read.append(str(path)+"/"+str(file.name))
            return files_to_read