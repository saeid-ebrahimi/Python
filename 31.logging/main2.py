import logging
from logging.handlers import TimeRotatingFileHandler
import time
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over s,m,h, midnight, w0-> monday w1-> tuesday
handler = TimeRotatingFileHandler("time_test.log",when='s',interval=5,backupCount=5)
for _ in range(10):
    logger.info("hello hell!")
    time.sleep(5)