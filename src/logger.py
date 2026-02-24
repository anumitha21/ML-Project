#recording what your program is doing (logs)

import logging
from datetime import datetime
import os

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log" #log file name with date and time
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) #log file path
os.makedirs(logs_path,exist_ok=True) #creating logs folder if not exist

LOG_FILE_PATH =os.path.join(logs_path,LOG_FILE) #full log file path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", #log message format
    level=logging.INFO, 
) #this is the format of log message and log level (INFO,DEBUG,ERROR) we can change it as per our need..which is the log output.

#we use like this
# logging.info("This is an info message")..and this is the info..which logged along witht the other messages.

#if __name__ == "__main__":
 #   logging.info("This is an info message")
  