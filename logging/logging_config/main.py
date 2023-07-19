# src/main.py
import logging
import logging.config
import os
from datetime import datetime

from processor import process_data
from dotenv import find_dotenv, load_dotenv
from trainer import train

# find .env file in parent directory
env_file = find_dotenv()
load_dotenv()

CONFIG_DIR = "./config"
LOG_DIR = "./logs"

def setup_logging():
    log_configs = {"dev": "logging.dev.ini", "prod": "logging.prod.ini"}
    config = log_configs.get(os.environ["ENV"], "logging.dev.ini")
    config_path = "/".join([CONFIG_DIR, config])

    timestamp = datetime.now().strftime("%Y%m%d-%H:%M:%S")

    logging.config.fileConfig(
        config_path,
        disable_existing_loggers=False,
        defaults={"logfilename": "C:/Users/adity/Desktop/DS_Projects/Python_Musings/logging_config/loggiot.log"},
    )

if __name__ == "__main__":

    setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("Program started")
    process_data()
    train()
    logger.info("Program finished")