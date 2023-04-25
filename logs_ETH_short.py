import sys
import logging

logger = logging.getLogger('')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('my_log_ETH_short.log')
sh = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(message)s          ETH SHORT BOT', datefmt='%a, %d %b %Y %H:%M:%S')
fh.setFormatter(formatter)
sh.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(sh)

def logg(text):
    logger.info(text)

