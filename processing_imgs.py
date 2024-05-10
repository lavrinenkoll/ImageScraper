import glob
import os

import imagehash
from PIL import Image


def calculate_image_hash(image_path):
    # Open the image and calculate the perceptual hash
    with Image.open(image_path) as img:
        hash_value = imagehash.average_hash(img)
    return hash_value


def is_small_image(image_path, min_width=70, min_height=70):
    # Check if the image dimensions are smaller than the specified thresholds
    with Image.open(image_path) as img:
        width, height = img.size
        if width < min_width or height < min_height:
            return True
    return False


def find_and_delete_duplicates(directory, min_width=70, min_height=70, extensions=('jpg', 'jpeg', 'png')):
    # Dictionary to store hashes and corresponding file paths
    hash_dict = {}

    # Iterate over all image files in the directory
    for ext in extensions:
        for image_file in glob.glob(os.path.join(directory, f'*.{ext}')):
            print(f"Processing file: {image_file}")
            # Check if the image is considered a small (junk) image
            if is_small_image(image_file, min_width, min_height):
                print(f"Junk image found: {image_file}. Deleting...")
                os.remove(image_file)
                continue  # Skip further processing for this image

            # Calculate hash for the image
            image_hash = calculate_image_hash(image_file)

            # Check if this hash already exists in the dictionary
            if image_hash in hash_dict:
                # Duplicate found, delete the duplicate file
                print(f"Duplicate found: {image_file}. Deleting...")
                os.remove(image_file)
            else:
                # Add hash and file path to dictionary
                hash_dict[image_hash] = image_file


if __name__ == "__main__":
    # Specify the directory containing images
    directory_path = 'imgs/лілії'

    # Call function to find and delete duplicates
    find_and_delete_duplicates(directory_path)

