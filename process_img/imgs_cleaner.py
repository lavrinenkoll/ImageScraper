import glob
import os
import time

import imagehash
from PIL import Image, ImageOps
from collections import defaultdict


class ImagesCleaner:
    def __init__(self, directory):
        self.directory = directory
        self.extensions = ('.jpg', '.jpeg', '.png')
        self.image_files = self.get_image_files()

    def get_image_files(self):
        image_files = []
        try:
            for file in os.listdir(self.directory):
                if file.endswith(self.extensions):
                    image_files.append(os.path.join(self.directory, file))
        except OSError as e:
            print(f"Error listing files in {self.directory}: {e}")
        return image_files

    def find_and_delete_small_images(self, min_width=50, min_height=50):
        self.image_files = self.get_image_files()
        for image_file in self.image_files:
            print(f"Processing file: {image_file}")
            try:
                with Image.open(image_file) as img:
                    width, height = img.size
                    if width < min_width or height < min_height:
                        print(f"Image is too small: {image_file}. Deleting...")
                        img.close()
                        self.delete_file(image_file)
            except (IOError, OSError, ValueError) as e:
                print(f"Error processing {image_file}: {e}")

    def find_and_delete_duplicates(self):
        self.image_files = self.get_image_files()
        hash_dict = defaultdict(list)

        for image_file in self.image_files:
            print(f"Processing file: {image_file}")
            image_hash = self.calculate_image_hash(image_file)

            if image_hash is not None:
                hash_dict[image_hash].append(image_file)

        for hash_value, duplicates in hash_dict.items():
            if len(duplicates) > 1:
                print(f"Duplicate images found: {duplicates}. Deleting...")
                for duplicate in duplicates[1:]:
                    self.delete_file(duplicate)

    def delete_mirror_duplicates(self, flip_direction='horizontal'):
        self.image_files = self.get_image_files()
        hash_dict = defaultdict(list)

        for image_file in self.image_files:
            print(f"Processing file: {image_file}")
            image_hash = self.calculate_image_hash(image_file)

            if image_hash is not None:
                hash_dict[image_hash].append(image_file)

            try:
                with Image.open(image_file) as img:
                    flipped_img = ImageOps.mirror(img) if flip_direction == 'horizontal' else ImageOps.flip(img)
                    flipped_hash = imagehash.average_hash(flipped_img)
            except (IOError, OSError, ValueError) as e:
                print(f"Error processing {image_file}: {e}")
                continue

            if flipped_hash is not None:
                hash_dict[flipped_hash].append(image_file)

        for hash_value, duplicates in hash_dict.items():
            if len(duplicates) > 1:
                print(f"Mirror duplicate images found: {duplicates}. Deleting...")
                for duplicate in duplicates[1:]:
                    self.delete_file(duplicate)

    def calculate_image_hash(self, image_path):
        try:
            with Image.open(image_path) as img:
                hash_value = imagehash.average_hash(img)
            return hash_value
        except (IOError, OSError, ValueError) as e:
            print(f"Error processing {image_path}: {e}")
            return None

    def delete_file(self, file_path, max_retries=3, retry_delay=1):
        retries = 0
        while retries < max_retries:
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    break  # File deleted successfully, exit the loop
                else:
                    print(f"File {file_path} not found.")
                    break
            except PermissionError:
                retries += 1
                print(f"PermissionError: Failed to delete {file_path}. Retrying ({retries}/{max_retries})...")
                time.sleep(retry_delay)
        else:
            print(f"Error: Could not delete {file_path} after {max_retries} retries.")

    def run(self, settings=(True, True, True, True)):
        if settings[0]:
            self.find_and_delete_small_images(min_width=70, min_height=70)
        if settings[1]:
            self.find_and_delete_duplicates()
        if settings[2]:
            self.delete_mirror_duplicates(flip_direction='horizontal')
        if settings[3]:
            self.delete_mirror_duplicates(flip_direction='vertical')


#
# def calculate_image_hash(image_path):
#     try:
#         with Image.open(image_path) as img:
#             hash_value = imagehash.average_hash(img)
#         return hash_value
#     except (IOError, OSError, ValueError) as e:
#         print(f"Error processing {image_path}: {e}")
#         return None
#
#
# def find_and_delete_small_images(directory, min_width=50, min_height=50, extensions=('jpg', 'jpeg', 'png')):
#
#     for ext in extensions:
#         for image_file in glob.glob(os.path.join(directory, f'*.{ext}')):
#             print(f"Processing file: {image_file}")
#             try:
#                 with Image.open(image_file) as img:
#                     width, height = img.size
#                     if width < min_width or height < min_height:
#                         print(f"Image is too small: {image_file}. Deleting...")
#                         img.close()
#                         delete_file(image_file)
#             except (IOError, OSError, ValueError) as e:
#                 print(f"Error processing {image_file}: {e}")
#
#
# def find_and_delete_duplicates(directory, extensions=('jpg', 'jpeg', 'png')):
#     # Dictionary to store hashes and corresponding file paths
#     hash_dict = {}
#
#     # Iterate over all image files in the directory
#     for ext in extensions:
#         for image_file in glob.glob(os.path.join(directory, f'*.{ext}')):
#             print(f"Processing file: {image_file}")
#
#             # Calculate hash for the image
#             image_hash = calculate_image_hash(image_file)
#
#             # Check if this hash already exists in the dictionary
#             if image_hash in hash_dict:
#                 # Duplicate found, delete the duplicate file
#                 print(f"Duplicate found: {image_file}. Deleting...")
#                 delete_file(image_file)
#             else:
#                 # Add hash and file path to dictionary
#                 hash_dict[image_hash] = image_file
#
#
# def delete_mirror_duplicates(directory, extensions=('jpg', 'jpeg', 'png'), flip_direction='horizontal'):
#     # Dictionary to store hashes and corresponding file paths
#     hash_dict = {}
#
#     # Iterate over all image files in the directory
#     for ext in extensions:
#         for image_file in glob.glob(os.path.join(directory, f'*.{ext}')):
#             print(f"Processing file: {image_file}")
#
#             # Calculate hash for the image
#             image_hash = calculate_image_hash(image_file)
#
#             # Check if this hash already exists in the dictionary
#             if image_hash in hash_dict:
#                 # Duplicate found, delete the duplicate file
#                 print(f"Mirror duplicate found: {image_file}. Deleting...")
#                 delete_file(image_file)
#             else:
#                 # Add hash and file path to dictionary
#                 hash_dict[image_hash] = image_file
#
#             # Calculate hash for the flipped image
#             try:
#                 with Image.open(image_file) as img:
#                     flipped_img = ImageOps.mirror(img) if flip_direction == 'horizontal' else ImageOps.flip(img)
#                     flipped_hash = imagehash.average_hash(flipped_img)
#             except (IOError, OSError, ValueError) as e:
#                 print(f"Error processing {image_file}: {e}")
#                 continue
#
#             # Check if the flipped hash already exists in the dictionary
#             if flipped_hash in hash_dict:
#                 # Mirror duplicate found, delete the duplicate file
#                 print(f"Mirror duplicate found: {image_file}. Deleting...")
#                 delete_file(image_file)
#             else:
#                 # Add flipped hash and file path to dictionary
#                 hash_dict[flipped_hash] = image_file
#
#
# def delete_file(file_path, max_retries=3, retry_delay=1):
#     retries = 0
#     while retries < max_retries:
#         try:
#             os.remove(file_path)
#             break  # File deleted successfully, exit the loop
#         except PermissionError:
#             retries += 1
#             print(f"PermissionError: Failed to delete {file_path}. Retrying ({retries}/{max_retries})...")
#             time.sleep(retry_delay)
#     else:
#         print(f"Error: Could not delete {file_path} after {max_retries} retries.")
#
#
# if __name__ == "__main__":
#     # Specify the directory containing images
#     directory_path = '../imgs/Leopard 2'
#
#     extensions = ('jpg', 'jpeg', 'png')
#
#     find_and_delete_small_images(directory_path, min_width=70, min_height=70, extensions=extensions)
#
#     find_and_delete_duplicates(directory_path, extensions=extensions)
#
#     delete_mirror_duplicates(directory_path, extensions=extensions, flip_direction='horizontal')
#     delete_mirror_duplicates(directory_path, extensions=extensions, flip_direction='vertical')
#
#

