import logging
import os

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:

    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    # Log file path
    log_file = os.path.join(log_dir, "bot.log")

    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create file handler to save logs to a file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # Create console handler for logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Define log format
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
