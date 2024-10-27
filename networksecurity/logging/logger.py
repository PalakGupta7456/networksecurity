import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

# Create a log filename with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path where logs will be stored
logs_dir = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Create a logger object
logger = logging.getLogger(__name__)

# Set the default logging level for the logger
logger.setLevel(logging.DEBUG)

# Create a file handler that logs messages to a file
file_handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=5*1024*1024, backupCount=5)
file_handler.setLevel(logging.INFO)  # Log level for file handler

# Create a stream handler to log messages to the console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)  # Log level for console handler

# Create a formatter and set it for both handlers
formatter = logging.Formatter("[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def get_logger():
    return logger

# from src.logger import get_logger
# logger=get_logger()

if __name__ == "__main__":
    # Example log messages
    logger.debug("This is a DEBUG level message (console only).")
    logger.info("This is an INFO level message (both console and file).")
    logger.warning("This is a WARNING level message (both console and file).")
    logger.error("This is an ERROR level message (both console and file).")
    logger.critical("This is a CRITICAL level message (both console and file).")
