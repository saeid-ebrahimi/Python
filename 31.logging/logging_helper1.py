import logging
logger = logging.getLogger(__name__)
# disable logging propagation after importing
logger.propagate = False
logger.info("Hello From Helper")

