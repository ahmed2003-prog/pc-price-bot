"""
This module sets up logging for the application.

Classes:
    LogLevel (Enum): Defines different log level options.

Functions:
    setup_logging(log_level: LogLevel = LogLevel.INFO) -> logging.Logger:
        Configures and returns a logger with the specified log level.

Usage:
    from logging_config import setup_logging, LogLevel
    logger = setup_logging(LogLevel.DEBUG)
    logger.info("Logging has been initialized.")
"""

import logging
from enum import Enum

class LogLevel(Enum):
    """Enum for defining different log levels."""
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

def setup_logging(log_level: LogLevel = LogLevel.INFO) -> logging.Logger:
    """
    Configures and returns a logger with a file and console handler.

    Args:
        log_level (LogLevel): The log level to be set (default: INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("ApplicationLogger")

    if logger.hasHandlers():
        return logger

    logger.setLevel(log_level.value)

    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_format)

    file_handler = logging.FileHandler("program.log", encoding="utf-8")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
