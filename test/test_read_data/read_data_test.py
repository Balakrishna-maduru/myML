import unittest
from pre_processing.read_data import ReadData


class ReadDataTest(unittest.TestCase):


    def test_get_files_to_read_file_path(self):
        print("Test")
        read_data = ReadData()
        self.assertEqual(read_data._get_files_to_read('data/ReadData/read_data.csv'),[1,2,3])


if __name__ == '__main__':
    unittest.main()