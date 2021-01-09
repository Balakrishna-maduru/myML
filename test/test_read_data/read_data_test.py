import unittest

class ReadData:

    def _get_files_to_read(self):
        return [1,2,3]


class ReadDataTest(unittest.TestCase):


    def test_get_files_to_read(self):
        print("Test")
        read_data = ReadData()
        self.assertEqual(read_data._get_file_to_read(),[1,2,3])


if __name__ == '__main__':
    pass
    