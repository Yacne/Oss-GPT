import logging

logging.basicConfig(
    filename="oss_gpt.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_error(message):
    logging.error(message)