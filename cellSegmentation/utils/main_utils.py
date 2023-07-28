import os.path
import sys
import yaml
import base64

from cellSegmentation.exception import AppException
from cellSegmentation.logger import logging


def read_yaml_file(file_path: str) -> dict:
    """
    Function to read a YAML file and return its content as a Python dictionary.

    :param file_path: The path to the YAML file.

    :return: A Python dictionary containing the content of the YAML file.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            # Log a message indicating that the YAML file is read successfully
            logging.info("Read yaml file successfully")
            # Load and return the content of the YAML file as a Python dictionary
            return yaml.safe_load(yaml_file)

    except Exception as e:
        # If an exception occurs, raise a custom 'AppException' with the original exception as the cause
        raise AppException(e, sys) from e

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Function to write data as YAML to a file.

    :param file_path: The path to the YAML file.
    :param content: The data to be written as YAML.
    :param replace: If True, replace the file if it already exists; otherwise, append to the existing file.

    :return: None
    """
    try:
        # If 'replace' is True and the file already exists, remove the existing file
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        # Create the directory structure to the file path if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Write the data as YAML to the file
        with open(file_path, "w") as file:
            yaml.dump(content, file)
            # Log a message indicating that the YAML file is written successfully
            logging.info("Successfully write_yaml_file")

    except Exception as e:
        # If an exception occurs, raise a custom 'AppException' with the original exception as the cause
        raise AppException(e, sys)

def decodeImage(imgstring, fileName):
    """
    Function to decode base64-encoded image data and save it as a file.

    :param imgstring: Base64-encoded image data.
    :param fileName: The name of the file to be saved.

    :return: None
    """
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    """
    Function to encode an image file into base64 format.

    :param croppedImagePath: The path to the image file.

    :return: The base64-encoded image data.
    """
    with open(croppedImagePath, "rb") as f:
        # Read the image file and encode it into base64 format
        return base64.b64encode(f.read())

    
    