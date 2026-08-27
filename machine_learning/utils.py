"""
utils.py

Utility functions used across the machine learning package.
"""

import os
import json
from datetime import datetime


def ensure_directory(path):
    """
    Create a directory if it doesn't exist.
    """
    os.makedirs(path, exist_ok=True)


def timestamp():
    """
    Return the current timestamp as a string.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def save_json(data, file_path):
    """
    Save a dictionary to a JSON file.
    """
    ensure_directory(os.path.dirname(file_path))

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_json(file_path):
    """
    Load a JSON file and return its contents.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def print_header(title):
    """
    Print a formatted console header.
    """
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


def normalize_percentage(value):
    """
    Clamp a value between 0 and 100.
    """
    return max(0.0, min(100.0, float(value)))