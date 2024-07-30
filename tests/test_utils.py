import unittest
import os
from src.utils.file_utils import list_files_in_directory

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_utils_files'
        os.makedirs(self.test_dir, exist_ok=True)
        self.test_file = os.path.join(self.test_dir, 'test.txt')
        with open(self.test_file, 'w') as f:
            f.write('Utility test file.')

    def tearDown(self):
        if os.path.exists(self.test_dir):
            for root, dirs, files in os.walk(self.test_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(self.test_dir)

    def test_list_files_in_directory(self):
        files = list_files_in_directory(self.test_dir)
        self.assertIn(self.test_file, files)

if __name__ == '__main__':
    unittest.main()
