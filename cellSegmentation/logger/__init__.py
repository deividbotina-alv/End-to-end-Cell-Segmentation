import logging
import os
from datetime import datetime
from from_root import from_root


# Create a log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%Y_%d_%m_%H_%M_%S')}.log"

# Get the path to the 'log' directory relative to the root of the project using the 'from_root' function
log_path = os.path.join(from_root(), 'log', LOG_FILE)

# Create the 'log' directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

# Create the full path to the log file
lOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure the logging module to write logs to the specified file
logging.basicConfig(
    filename=lOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)




