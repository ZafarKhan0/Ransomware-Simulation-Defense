import logging

class Logger:
    def __init__(self, log_file='ransomware_simulation.log'):
        logging.basicConfig(filename=log_file, level=logging.INFO)

    def log(self, message):
        logging.info(message)