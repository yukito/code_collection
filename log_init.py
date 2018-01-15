import logging

LOG_LEVEL = logging.DEBUG
LOG_FILE = "/tmp/sample.log"


def log_init(namespace = ""):
   logger = logging.getLogger(namespace)
   logger.setLevel(LOG_LEVEL)
   handler = logging.FileHandler(LOG_FILE)
   formatter = logging.Formatter('%(asctime)s %(levelname)s:%(name)s %(message)s')
   handler.setFormatter(formatter)
   handler.setLevel(LOG_LEVEL)
   logger.addHandler(handler)
   return logger
