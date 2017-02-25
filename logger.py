"""
Logger for PlexDownloader
"""
import logging
import logging.handlers as lh

LOGFILENAME = 'PlexDownloader.log'
LOGFILESTOKEEP = 4
LOGFORMAT = '%(asctime)-15s [%(levelname)s] %(message)s'
ROTATIONSIZE = 5242880  # Rotate the logfile at 5MB

logger = logging.getLogger('plexdownloader')
logger.setLevel(logging.DEBUG)
fh = lh.RotatingFileHandler(
    LOGFILENAME, maxBytes=ROTATIONSIZE, backupCount=LOGFILESTOKEEP, encoding='utf-8')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(LOGFORMAT)
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

# logger.warning('Test log: %s', 'Test only')
