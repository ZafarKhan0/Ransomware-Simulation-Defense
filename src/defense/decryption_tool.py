import sys
import os
from src.simulation.file_encryptor import FileEncryptor
from cryptography.fernet import Fernet

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))




class DecryptionTool:
    def __init__(self, target_dir, key):
        self.target_dir = target_dir
        self.key = key.encode()  # Ensure the key is bytes
        self.cipher = Fernet(self.key)

    def decrypt_file(self, file_path):
        print(f"Decrypting file: {file_path}")
        try:
            with open(file_path, 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = self.cipher.decrypt(encrypted_data)
            with open(file_path, 'wb') as file:
                file.write(decrypted_data)
        except Exception as e:
            print(f"Failed to decrypt {file_path}: {e}")

    def decrypt_all_files(self):
        for root, _, files in os.walk(self.target_dir):
            for file in files:
                file_path = os.path.join(root, file)
                self.decrypt_file(file_path)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Ransomware decryption tool.")
    parser.add_argument("--target-dir", required=True, help="The directory containing the encrypted files.")
    parser.add_argument("--key", required=True, help="The encryption key used to decrypt the files.")
    args = parser.parse_args()

    decryption_tool = DecryptionTool(target_dir=args.target_dir, key=args.key)
    decryption_tool.decrypt_all_files()
