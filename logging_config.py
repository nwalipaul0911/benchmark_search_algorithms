"""
This module houses the logging handlers for file logging and console logging.
"""

import logging
import sys
from logging.handlers import RotatingFileHandler

# --- File handler with rotation ---
file_handler = RotatingFileHandler(
    "app.log", mode="a", maxBytes=5000 * 1024 * 1024,
    backupCount=1000, encoding="utf-8"
)

# --- Console handler ---
console_handler = logging.StreamHandler(sys.stdout)

# --- Formatter ---
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
