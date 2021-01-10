import sys
import os
sys.path.append('C:/Users/mabalakr/source/repos/myML/')
import unittest
import pandas as pd
from pathlib import Path

from pre_processing.read_data import ReadData
from common_methods_test import CommonMethodsTest


class ReadDataTest(unittest.TestCase):

    def setUp(self):
        self.sample_file = os.path.abspath(__file__)
        self.resources_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(self.sample_file))),"resources")


    def test_get_files_to_read_file_path_single_file(self):
        file_name = self.resources_path+'/data/ReadData/read_data.csv'
        read_data = ReadData()
        self.assertEqual(read_data._get_files_to_read(file_name),[file_name])


    def test_get_files_to_read_file_path_multiple_files(self):
        file_name = self.resources_path+'/data/ReadData/'
        read_data = ReadData()
        common_methods = CommonMethodsTest()
        self.assertEqual(read_data._get_files_to_read(file_name),common_methods._get_file_names_as_list(file_name))

    def test_read_data_single_file(self):
        file_name = self.resources_path+'/data/ReadData/read_data.csv'
        read_data = ReadData()
        self.assertEqual(isinstance(read_data.read(file_name),pd.DataFrame),True)

    def test_read_data_multipe_file(self):
        file_name = self.resources_path+'/data/ReadData/'
        read_data = ReadData()
        self.assertEqual(isinstance(read_data.read(file_name),pd.DataFrame),True)




if __name__ == '__main__':
    unittest.main()