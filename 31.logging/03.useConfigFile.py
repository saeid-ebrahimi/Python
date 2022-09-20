import logging
import logging.config
import logging
logging.config.fileConfig( "logging.conf" )
logger = logging.getLogger('simpleExample')
logger.debug("this is debug message")
