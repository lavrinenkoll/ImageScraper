import os
import imagehash
from PIL import Image, ImageOps
from collections import defaultdict
from tools.file_manager import FileManager


class ImagesCleaner:
    def __init__(self, directory, save_deleted=False):
        self.directory = directory
        self.extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')
        self.file_manager = FileManager(directory)
        self.save_deleted = save_deleted
        self.image_files = []

    def find_and_delete_one_color_images(self):
        self.image_files = self.file_manager.get_image_files()
        for image_file in self.image_files:
            print(f"Processing file: {image_file}")
            try:
                with Image.open(image_file) as img:
                    img = img.convert('RGB')
                    colors = img.getcolors()
                    if colors is not None and len(colors) == 1:
                        print(f"Image is one color: {image_file}. Deleting...")
                        img.close()
                        self.file_manager.delete_file(image_file, save_deleted=self.save_deleted)
                    else:
                        img.close()
            except (IOError, OSError, ValueError) as e:
                print(f"Error processing {image_file}: {e}")

    def find_and_delete_small_images(self, min_width=50, min_height=50):
        self.image_files = self.file_manager.get_image_files()
        for image_file in self.image_files:
            print(f"Processing file: {image_file}")
            try:
                with Image.open(image_file) as img:
                    width, height = img.size
                    if width < min_width or height < min_height:
                        print(f"Image is too small: {image_file}. Deleting...")
                        img.close()
                        self.file_manager.delete_file(image_file)
            except (IOError, OSError, ValueError) as e:
                print(f"Error processing {image_file}: {e}")

    def find_and_delete_duplicates(self):
        self.image_files = self.file_manager.get_image_files()
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
                    self.file_manager.delete_file(duplicate, save_deleted=self.save_deleted)

    def delete_mirror_duplicates(self, flip_direction='horizontal'):
        self.image_files = self.file_manager.get_image_files()
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
                    self.file_manager.delete_file(duplicate, save_deleted=self.save_deleted)

    @staticmethod
    def calculate_image_hash(image_path):
        try:
            with Image.open(image_path) as img:
                hash_value = imagehash.average_hash(img)
            return hash_value
        except (IOError, OSError, ValueError) as e:
            print(f"Error processing {image_path}: {e}")
            return None

    def run(self, find_and_delete_one_color_images=True,
            delete_small_images=True, min_width=70, min_height=70,
            delete_duplicates=True,
            delete_mirror_duplicates_horizontal=True,
            delete_mirror_duplicates_vertical=True,
            delete_mirror_duplicates_vertical_horizontal=True):
        if find_and_delete_one_color_images:
            self.find_and_delete_one_color_images()
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
