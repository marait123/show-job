import logging
import sys


def get_logger(logger_name="tmp", log_level=logging.DEBUG) -> logging.Logger:
    logger = logging.getLogger(logger_name)

    # If the logger already has handlers, don't add more
    if logger.handlers:
        logger.handlers.clear()

    logger.setLevel(log_level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.propagate = False

    return logger
