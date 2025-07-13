from src.exception import CustomException
import sys
from src.logger import logging

try:
    raise Exception("this is a test error") #error

except Exception as e:
    CustomExce = CustomException(e,sys)
    logging.info(CustomExce.error_message)
    logging.info("testing exception")

print('test')