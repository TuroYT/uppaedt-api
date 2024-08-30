import logging

class Logger:
    def __init__(self):
        
        logging.basicConfig(filename="uppa-api.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
        self.logger = logging.getLogger("uppa-api")
        
    def info(self, message):
        self.logger.info(message)
    def error(self, message):
        self.logger.error(message)
    def warning(self, message):
        self.logger.warning(message)
    def debug(self, message):
        self.logger.debug(message)
    def critical(self, message):
        self.logger.critical(message)
    def exception(self, message):
        self.logger.exception(message)
    def log(self, level, message):
        self.logger.log(level, message)

        
        