Ransomware Simulation and Defense

Overview
The Ransomware Simulation and Defense project provides a simulation tool to mimic ransomware attacks and a defense mechanism to decrypt the encrypted files. This project is designed to help everyone understand ransomware attacks, test their defenses, and practice recovery procedures.

Features
-Simulation of Ransomware Attacks: Mimics ransomware behavior by encrypting files and leaving a ransom note.
-Decryption Tool: Provides a way to decrypt files using the correct key.
-Key Management: Generates and manages encryption keys for secure file handling.
-Backup Manager: Create and manage backups before simulating attacks.
-Ransomware Detection: Detect ransomware activity and alert users.
-Testing Framework: Run tests to validate the functionality of the tools.

Prerequisites
-Python 3.8 or later
-Required Python libraries

Installation
-Clone the Repository
  git clone https://github.com/ZafarKhan0/Ransomware-Simulation-Defense.git
-cd Ransomware-Simulation-Defense

Install Dependencies
-Create and activate a virtual environment:
  -python -m venv venv
  -source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required Python libraries:
-pip install -r requirements.txt

Usage
1. Backup Management
To create a backup before simulating an attack:

Command:
-python src/defense/backup_manager.py --target-dir <TARGET_DIRECTORY> --backup-dir <BACKUP_DIRECTORY>

Parameters:
--target-dir: Path to the directory containing files to back up.
--backup-dir: Path to the directory where backups will be stored.

Example:
python src/defense/backup_manager.py --target-path "D:\ZafarKhan_projects\blockchain_secure_file_sharing" --backup-dir "D:\ZafarKhan_projects\backups"

2. Simulate Ransomware Attack
To simulate a ransomware attack, use the payload.py script. This script will encrypt files in a specified directory and create a ransom note.

Command:
-python src/simulation/payload.py --target-dir <TARGET_DIRECTORY> --ransom-note <RANSOM_NOTE_FILE>

Parameters:
  --target-dir: Path to the directory containing files to encrypt.
  --ransom-note: Path to the ransom note file.

Example:
 -python src/simulation/payload.py --target-dir "D:\ZafarKhan_projects\blockchain_secure_file_sharing" --ransom-note "ransom_note.txt"


4. Decrypt Files
To decrypt files that have been encrypted, use the decryption_tool.py script. You need to provide the correct encryption key and the target directory containing the encrypted files.

Command:
-python src/defense/decryption_tool.py --target-dir <TARGET_DIRECTORY> --key <ENCRYPTION_KEY>

Parameters:
--target-dir: Path to the directory containing encrypted files.
--key: Base64 URL-safe encryption key used for decryption.

Example:
python src/defense/decryption_tool.py --target-dir "D:\ZafarKhan_projects\blockchain_secure_file_sharing" --key "wQcl3iK3AEB4cn4vMGN9e7PcTV2vO5K3z2SPa1WzEmk="


5. Ransomware Detection
To detect ransomware activity:

Command:
python src/detection/ransomware_detector.py --target-dir <TARGET_DIRECTORY>

Parameters:
--target-dir: Path to the directory where ransomware activity will be detected.

Example:
python src/detection/ransomware_detector.py --target-dir "D:\ZafarKhan_projects\blockchain_secure_file_sharing"

6. Run Tests
To ensure all components are working correctly, run the tests:

Command:
pytest
This command will execute all tests located in the tests/ directory.

Contributing
Contributions are welcome! Please follow these steps:
-Fork the repository.
-Create a new branch for your feature or fix.
-Make your changes.
-Commit and push your changes.
-Open a pull request.

Contact
For questions or issues, please contact K213567@nu.edu.pk.