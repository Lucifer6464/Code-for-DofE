import logging

# this will create a logger with the name of the file as the name
logger = logging.getLogger(__name__)
# all loggers, by default, have a hierarchy of logger with the root logger at the top
# by setting logger.propagate=False you will stop it from doing this and it will not propagate to the
# base logger and nothing will be locked if you import it into another file
# logger.propagate = False
logger.info('hello from logger')
