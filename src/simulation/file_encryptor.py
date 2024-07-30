from cryptography.fernet import Fernet

class FileEncryptor:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            encrypted_data = self.cipher.encrypt(file.read())
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            decrypted_data = self.cipher.decrypt(file.read())
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)

    def get_key(self):
        return self.key
