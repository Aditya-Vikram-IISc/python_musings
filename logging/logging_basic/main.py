# src/main.py
import logging
import sys
from trainer import train
from processor import process_data


logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.info("Program started")
    process_data()
    train()
    logger.info("Program finished")