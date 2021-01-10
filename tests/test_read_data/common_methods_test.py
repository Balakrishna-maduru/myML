import os

class CommonMethodsTest:

    def _get_file_names_as_list(self, path):
        files_list = []
        for bdir,sdir, files in os.walk(path):
            for file in files:
                files_list.append(bdir+"/"+file)
        return files_list
