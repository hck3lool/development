import logging


def set_logging_options():
    logging_format = ' %(levelname)5s - %(asctime)s - %(funcName)s - - %(message)s'
    logging.basicConfig(level=logging.INFO, format=logging_format)
