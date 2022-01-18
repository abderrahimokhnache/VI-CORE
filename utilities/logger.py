import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = 'issues.log' , level = logging.DEBUG,
	format = LOG_FORMAT )

logger = logging.getLogger()

def log(ex) :
    logger.error(ex)
