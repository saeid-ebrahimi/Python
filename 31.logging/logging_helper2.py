import logging
logger = logging.getLogger(__name__)
logger.propagate = False

# create handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("file.log")

# level and the format
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# add handler
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
"""
logger.warning("this a warning")
logger.error("this is an error")"""

