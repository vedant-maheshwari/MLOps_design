import logging
import os, sys
from datetime import datetime

LOG_DIR = 'logs'
# #os.getcwd() gets the current working directory
# #creating a log dir to store logs
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

# #creating log dir
os.makedirs(LOG_DIR, exist_ok=True)


# #creating file name convention to store logs
# # .log log_2025_..
CURRENT_TIME_STAMP = f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'
# file name : log_2025-07-13-14-48-49.log
FILE_NAME = f'log_{CURRENT_TIME_STAMP}.log'

LOG_FILE_PATH = os.path.join(LOG_DIR,FILE_NAME)

#when log will be created how will it disply -> time name - level(INFO,ERROR etc.) - message
#[2025-07-13 14:48:49,935] schema - INFO - This is a test log from main.py
LOGGING_FORMAT = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s'

#handlers in python tells you where the log will go i.e. terminal, file, email, server etc.
#for loggin in terminal use logging.StreamHandler() and for file use logging.FileHandler()
#can directly use file handler just by defining filepath and no use of handler param
logging.basicConfig(format = LOGGING_FORMAT,
                    level=logging.INFO,
                    handlers=[
                        logging.FileHandler(LOG_FILE_PATH),
                        # logging.StreamHandler()
                        ]
                    )


