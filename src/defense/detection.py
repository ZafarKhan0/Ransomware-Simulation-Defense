import os

class Detection:
    def __init__(self):
        self.detected_files = []

    def detect_ransomware_activity(self, target_dir):
        for root, dirs, files in os.walk(target_dir):
            for file in files:
                if file.endswith('.encrypted'):
                    self.detected_files.append(os.path.join(root, file))

        return self.detected_files

if __name__ == "__main__":
    detector = Detection()
    infected_files = detector.detect_ransomware_activity(target_dir='/path/to/scan')
    for file in infected_files:
        print(f'Detected ransomware activity: {file}')
