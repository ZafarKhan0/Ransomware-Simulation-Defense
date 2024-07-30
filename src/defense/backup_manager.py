import argparse
import os
import shutil

class BackupManager:
    def __init__(self, source_path, backup_dir):
        self.source_path = source_path
        self.backup_dir = backup_dir

    def create_backup(self):
        if not os.path.exists(self.source_path):
            raise FileNotFoundError(f"Source path {self.source_path} does not exist.")
        
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

        backup_path = os.path.join(self.backup_dir, os.path.basename(self.source_path))
        
        if os.path.isdir(self.source_path):
            if os.path.exists(backup_path):
                shutil.rmtree(backup_path)
            shutil.copytree(self.source_path, backup_path)
        else:
            shutil.copy2(self.source_path, backup_path)
        
        print(f"Backup created at {backup_path}")

def main():
    parser = argparse.ArgumentParser(description='Create a backup of the target file or directory.')
    parser.add_argument('--target-path', required=True, help='File or directory to back up.')
    parser.add_argument('--backup-dir', required=True, help='Directory to store the backup.')
    
    args = parser.parse_args()
    
    backup_manager = BackupManager(source_path=args.target_path, backup_dir=args.backup_dir)
    backup_manager.create_backup()

if __name__ == '__main__':
    main()
