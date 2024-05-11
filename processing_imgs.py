import glob
import os
import shutil
import time

import cv2
import imagehash
import numpy as np
from PIL import Image, ImageOps
from collections import defaultdict


def calculate_image_hash(image_path):
    try:
        with Image.open(image_path) as img:
            hash_value = imagehash.average_hash(img)
        return hash_value
    except (IOError, OSError, ValueError) as e:
        print(f"Error processing {image_path}: {e}")
        return None


def find_and_delete_small_images(directory, min_width=50, min_height=50, extensions=('jpg', 'jpeg', 'png')):

    for ext in extensions:
        for image_file in glob.glob(os.path.join(directory, f'*.{ext}')):
            print(f"Processing file: {image_file}")
            try:
                with Image.open(image_file) as img:
                    width, height = img.size
                    if width < min_width or height < min_height:
                        print(f"Image is too small: {image_file}. Deleting...")
                        img.close()
                        delete_file(image_file)
            except (IOError, OSError, ValueError) as e:
                print(f"Error processing {image_file}: {e}")


def find_and_delete_duplicates(directory, extensions=('jpg', 'jpeg', 'png')):
    # Dictionary to store hashes and corresponding file paths
    hash_dict = {}

    # Iterate over all image files in the directory
    for ext in extensions:
        for image_file in glob.glob(os.path.join(directory, f'*.{ext}')):
            print(f"Processing file: {image_file}")

            # Calculate hash for the image
            image_hash = calculate_image_hash(image_file)

            # Check if this hash already exists in the dictionary
            if image_hash in hash_dict:
                # Duplicate found, delete the duplicate file
                print(f"Duplicate found: {image_file}. Deleting...")
                delete_file(image_file)
            else:
                # Add hash and file path to dictionary
                hash_dict[image_hash] = image_file


def delete_mirror_duplicates(directory, extensions=('jpg', 'jpeg', 'png'), flip_direction='horizontal'):
    # Dictionary to store hashes and corresponding file paths
    hash_dict = {}

    # Iterate over all image files in the directory
    for ext in extensions:
        for image_file in glob.glob(os.path.join(directory, f'*.{ext}')):
            print(f"Processing file: {image_file}")

            # Calculate hash for the image
            image_hash = calculate_image_hash(image_file)

            # Check if this hash already exists in the dictionary
            if image_hash in hash_dict:
                # Duplicate found, delete the duplicate file
                print(f"Mirror duplicate found: {image_file}. Deleting...")
                delete_file(image_file)
            else:
                # Add hash and file path to dictionary
                hash_dict[image_hash] = image_file

            # Calculate hash for the flipped image
            try:
                with Image.open(image_file) as img:
                    flipped_img = ImageOps.mirror(img) if flip_direction == 'horizontal' else ImageOps.flip(img)
                    flipped_hash = imagehash.average_hash(flipped_img)
            except (IOError, OSError, ValueError) as e:
                print(f"Error processing {image_file}: {e}")
                continue

            # Check if the flipped hash already exists in the dictionary
            if flipped_hash in hash_dict:
                # Mirror duplicate found, delete the duplicate file
                print(f"Mirror duplicate found: {image_file}. Deleting...")
                delete_file(image_file)
            else:
                # Add flipped hash and file path to dictionary
                hash_dict[flipped_hash] = image_file


def delete_file(file_path, max_retries=3, retry_delay=1):
    retries = 0
    while retries < max_retries:
        try:
            os.remove(file_path)
            break  # File deleted successfully, exit the loop
        except PermissionError:
            retries += 1
            print(f"PermissionError: Failed to delete {file_path}. Retrying ({retries}/{max_retries})...")
            time.sleep(retry_delay)
    else:
        print(f"Error: Could not delete {file_path} after {max_retries} retries.")


if __name__ == "__main__":
    # Specify the directory containing images
    directory_path = 'imgs/Leopard 2'

    extensions = ('jpg', 'jpeg', 'png')

    find_and_delete_small_images(directory_path, min_width=70, min_height=70, extensions=extensions)

    find_and_delete_duplicates(directory_path, extensions=extensions)

    delete_mirror_duplicates(directory_path, extensions=extensions, flip_direction='horizontal')
    delete_mirror_duplicates(directory_path, extensions=extensions, flip_direction='vertical')



