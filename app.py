from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
import sys


try:
    3/0
except Exception as e:
    logging.info("La cagates")
    raise AppException(e, sys)