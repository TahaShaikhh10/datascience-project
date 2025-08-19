import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
     
    Reads a YAML file and returns
    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
       raise ValueError("YAML file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        ignore_logs (bool): Ignore if multiple dirs is to be created.

    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"created directory at: {path}")
        except Exception as e:
            logger.error(f"Error creating directory {path}: {e}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path(Path): path to json file
        data(dict): data to be saved in json file
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")
    


@ensure_annotations
def load_json(path: Path) -> dict:
    """Load JSON data from a file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        dict: The loaded JSON data.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file successfully loaded from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save data to a binary file using joblib.

    Args:
        data (Any): Data to be saved as binary
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Data saved as binary at: {path}")
    return data