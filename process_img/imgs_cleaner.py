import os
import shutil
import time
import imagehash
from PIL import Image, ImageOps
from collections import defaultdict


class ImagesCleaner:
    def __init__(self, directory, save_deleted=False):
        self.directory = directory
        self.extensions = ('.jpg', '.jpeg', '.png')
        self.image_files = self.get_image_files()
        self.save_deleted = save_deleted

    def get_image_files(self):
        image_files = []
        try:
            for file in os.listdir(self.directory):
                if file.endswith(self.extensions):
                    image_files.append(os.path.join(self.directory, file))
        except OSError as e:
            print(f"Error listing files in {self.directory}: {e}")
        return image_files

    def find_and_delete_trash_images(self, white_images=True, black_images=True):
        self.image_files = self.get_image_files()
        for image_file in self.image_files:
            print(f"Processing file: {image_file}")
            try:
                with Image.open(image_file) as img:
                    grayscale_img = img.convert('L')
                    is_all_white = all(pixel == 255 for pixel in grayscale_img.getdata())
                    is_all_black = all(pixel == 0 for pixel in grayscale_img.getdata())
                    if white_images and is_all_white:
                        print(f"Image is all white: {image_file}. Deleting...")
                        self.delete_file(image_file)
                    if black_images and is_all_black:
                        print(f"Image is all black: {image_file}. Deleting...")
                        self.delete_file(image_file)
            except (IOError, OSError, ValueError) as e:
                print(f"Error processing {image_file}: {e}")

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
                    flipped_img_horizontal = ImageOps.mirror(img)
                    flipped_img_vertical = ImageOps.flip(img)
                    flipped_img_both = ImageOps.mirror(flipped_img_vertical)

                    flipped_hash_horizontal = imagehash.average_hash(flipped_img_horizontal)
                    flipped_hash_vertical = imagehash.average_hash(flipped_img_vertical)
                    flipped_hash_both = imagehash.average_hash(flipped_img_both)

                    if flip_direction == 'horizontal':
                        hash_dict[flipped_hash_horizontal].append(image_file)
                    elif flip_direction == 'vertical':
                        hash_dict[flipped_hash_vertical].append(image_file)
                    elif flip_direction == 'vertical-horizontal':
                        hash_dict[flipped_hash_both].append(image_file)
                    else:
                        pass
            except (IOError, OSError, ValueError) as e:
                print(f"Error processing {image_file}: {e}")
                continue

        for hash_value, duplicates in hash_dict.items():
            if len(duplicates) > 1:
                shortest_file = min(duplicates, key=lambda x: len(os.path.basename(x)))
                files_to_delete = [file for file in duplicates if file != shortest_file]

                for duplicate in files_to_delete:
                    self.delete_file(duplicate)

    @staticmethod
    def calculate_image_hash(image_path):
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

                    if self.save_deleted:
                        deleted_folder = os.path.join(self.directory, 'deleted')
                        os.makedirs(deleted_folder, exist_ok=True)
                        file_name = os.path.basename(file_path)
                        deleted_file_path = os.path.join(deleted_folder, file_name)
                        shutil.copyfile(file_path, deleted_file_path)

                    os.remove(file_path)
                    break
                else:
                    print(f"File {file_path} not found.")
                    break
            except PermissionError:
                retries += 1
                print(f"PermissionError: Failed to delete {file_path}. Retrying ({retries}/{max_retries})...")
                time.sleep(retry_delay)
        else:
            print(f"Error: Could not delete {file_path} after {max_retries} retries.")

    def run(self, find_and_delete_trash_images=True, white_images=True, black_images=True,
            delete_small_images=True, min_width=70, min_height=70,
            delete_duplicates=True,
            delete_mirror_duplicates_horizontal=True,
            delete_mirror_duplicates_vertical=True,
            delete_mirror_duplicates_vertical_horizontal=True):
        if find_and_delete_trash_images:
            self.find_and_delete_trash_images(white_images, black_images)
        if delete_small_images:
            self.find_and_delete_small_images(min_width, min_height)
        if delete_duplicates:
            self.find_and_delete_duplicates()
        if delete_mirror_duplicates_horizontal:
            self.delete_mirror_duplicates(flip_direction='horizontal')
        if delete_mirror_duplicates_vertical:
            self.delete_mirror_duplicates(flip_direction='vertical')
        if delete_mirror_duplicates_vertical_horizontal:
            self.delete_mirror_duplicates(flip_direction='vertical-horizontal')
