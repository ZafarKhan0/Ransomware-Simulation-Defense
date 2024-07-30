import unittest
import os
from src.defense.backup_manager import BackupManager
from src.defense.decryption_tool import DecryptionTool
from src.simulation.file_encryptor import FileEncryptor

class TestDefense(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_files'
        self.backup_dir = 'backup'
        os.makedirs(self.test_dir, exist_ok=True)
        self.test_file = os.path.join(self.test_dir, 'test.txt')
        with open(self.test_file, 'w') as f:
            f.write('This is a test file.')

        self.backup_manager = BackupManager(backup_dir=self.backup_dir)
        self.encryptor = FileEncryptor()
        self.encryptor.encrypt_file(self.test_file)
        self.encrypted_file_content = open(self.test_file, 'rb').read()

    def tearDown(self):
        if os.path.exists(self.test_dir):
            for root, dirs, files in os.walk(self.test_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(self.test_dir)

        if os.path.exists(self.backup_dir):
            for root, dirs, files in os.walk(self.backup_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(self.backup_dir)

    def test_create_backup(self):
        self.backup_manager.create_backup(source_dir=self.test_dir)
        backup_path = os.path.join(self.backup_dir, 'test_files', 'test.txt')
        self.assertTrue(os.path.exists(backup_path))

    def test_decrypt_files(self):
        decryption_tool = DecryptionTool(key=self.encryptor.get_key())
        decryption_tool.decrypt_files(target_dir=self.test_dir)
        with open(self.test_file, 'r') as f:
            content = f.read()
        self.assertEqual(content, 'This is a test file.')

if __name__ == '__main__':
    unittest.main()
