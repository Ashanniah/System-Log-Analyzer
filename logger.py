import logging
from pathlib import Path


def setup_logger(path: Path) -> logging.Logger:
    logger = logging.getLogger("SystemLogAnalyzer")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler = logging.FileHandler(path, encoding="utf-8")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
