import logging

LOG_LEVEL = logging.DEBUG
LOG_FILE = "/tmp/sample.log"

loggers = {}


def log_init(namespace = __name__):

    if namespace in loggers:
        return loggers[namespace]

    logger = logging.getLogger(namespace)
    logger.setLevel(LOG_LEVEL)
    handler = logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter('%(asctime)s %(levelname)s:%(name)s %(message)s')
    handler.setFormatter(formatter)
    handler.setLevel(LOG_LEVEL)
    logger.addHandler(handler)
    logger.propagate = True

    loggers[namespace] = logger
    logger.debug(namespace + " has been initialized")

    return logger

# Following is for those who use syslog

import logging.handlers

def log_init():

   logger = logging.getLogger("load_checker")
   logger.setLevel(LOG_LEVEL)

   handler = logging.handlers.SysLogHandler(address = LOG_SERVER, facility="local7")
   formatter = logging.Formatter('%(asctime)s %(levelname)s:%(name)s %(message)s')
   handler.setFormatter(formatter)
   handler.setLevel(LOG_LEVEL)
   logger.addHandler(handler)
   logger.propagate = True

   return logger

