import unittest
import os
from src.simulation.file_encryptor import FileEncryptor
from src.simulation.ransomware_simulation import RansomwareSimulation

class TestRansomwareSimulation(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_files'
        os.makedirs(self.test_dir, exist_ok=True)
        self.test_file = os.path.join(self.test_dir, 'test.txt')
        with open(self.test_file, 'w') as f:
            f.write('This is a test file.')
        self.simulation = RansomwareSimulation(target_dir=self.test_dir)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            for root, dirs, files in os.walk(self.test_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(self.test_dir)

    def test_encrypt_files(self):
        self.simulation.simulate_attack()
        with open(self.test_file, 'rb') as f:
            content = f.read()
        # Check if the file is encrypted (not equal to original content)
        self.assertNotEqual(content, b'This is a test file.')

    def test_generate_ransom_note(self):
        ransom_note = os.path.join(self.test_dir, 'README.txt')
        self.simulation.generate_ransom_note(note_path=ransom_note)
        self.assertTrue(os.path.exists(ransom_note))

if __name__ == '__main__':
    unittest.main()
