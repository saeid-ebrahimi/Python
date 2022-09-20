import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB and keep logs app,log,1, app,log,2 , etc.

handler = RotatingFileHandler("app.log",maxBytes=2000,backupCount=5)
logger.addHandler(handler)

for _ in range(1000):
    logger.info("hello hell!")