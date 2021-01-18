import logging

# information for basicConfig can be found in the documentation but it just makes logging messages look
# much better and give more information about the date, time, names and message

# the datefmt (dateformat) will lock the time as well as everything else being logged to that value by the root
# locker. If you want to log if other modules it is best not to use the root logger and to instead create
# your own logger as has been done in 3.1 Logging Helper
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

logging.debug('debug message')
logging.info('info message')
# by default only messages with the level of warning or above will be printed
# you can change this by changing the basic config
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
from logs import HelperToLogging
# log handler (error messages when something happens they will produce a result of an error message
# for warning and error for a file or stream

logger = logging.getLogger(__name__)

# create handler for the screen and files
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('logs/file.log')

# level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

# what level they should be raised at
logger.warning('warning')
logger.error('error')

# there are other config methods such as the file and dict config methods
# to create these, you have to create a logging.conf file and define the
# loggers, handler, formatters, logger_root and arguments for it for cleaner code
# to use it you import logging.config and then call
# logging.config.fileConfig('logging.conf') and then you can create
# a logger the name of a logger in the file and use this at a certain level
# the dict config can be seen in the documentation

# we can log certain errors this way
try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    # the can log the error message and then also the stacktrace (where the error is)
    logging.error(e, exc_info=True)

# or you can format it using a traceback method (it does the same thing)
import traceback

try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    # the can log the error message and then also the stacktrace (where the error is)
    logging.error('The error is %s', traceback.format_exc())

# a rotating file handler
from logging.handlers import RotatingFileHandler

# this is useful for programs where you have lots of log handlers and you
# want to keep track of the most recent events

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB and keep backup logs app.log.1, app.log.2 e.t.c.
handler = RotatingFileHandler('logs/app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('hello world')

# if your program is expected to run for a long time then you can use a TimedRotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# it will create a file every 5 seconds and will have a backup of 5 files
handler = TimedRotatingFileHandler('logs/timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('hello world')
    time.sleep(5)
