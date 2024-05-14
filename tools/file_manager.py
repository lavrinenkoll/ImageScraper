import os
import shutil
import time
from io import BytesIO

import requests
from PIL import Image


class FileManager:
    def __init__(self):
        #self.directory = directory
        self.extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')

    def get_image_files(self, directory):
        image_files = []
        try:
            for file in os.listdir(directory):
                if file.endswith(self.extensions):
                    image_files.append(os.path.join(directory, file))
        except OSError as e:
            print(f"Error listing files in {directory}: {e}")
        return image_files

    def extract_images_from_folders(self, directory):
        subdirectories = [os.path.join(directory, d) for d in os.listdir(directory) if
                          os.path.isdir(os.path.join(directory, d))]

        for subdir in subdirectories:
            for file in os.listdir(subdir):
                if file.endswith(self.extensions):
                    source_path = os.path.join(subdir, file)
                    destination_path = os.path.join(directory, file)

                    shutil.move(source_path, destination_path)

            if not os.listdir(subdir):
                os.rmdir(subdir)

    @staticmethod
    def delete_file(file_path, max_retries=3, retry_delay=1, save_deleted=False):
        retries = 0
        while retries < max_retries:
            try:
                if os.path.exists(file_path):

                    if save_deleted:
                        path = os.path.split(file_path)
                        deleted_folder = os.path.join(path[0], 'deleted')
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

    @staticmethod
    def move_files_to_folders(folder_files_map):
        for folder, files in folder_files_map.items():
            os.makedirs(folder, exist_ok=True)
            for file in files:
                try:
                    shutil.move(file, folder)
                except Exception as e:
                    continue

    @staticmethod
    def save_img_from_url(url, path):
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            os.makedirs(path, exist_ok=True)
            img.save(f"{path}/{url.split('/')[-1]}")
            print(f"Succesfully processed image {url}")
        except Exception as e:
            print(f"Error processing image {url}: {e}")

    @staticmethod
    def save_links_to_file(links, query, path_to_save=None):
        if path_to_save is not None:
            os.makedirs(path_to_save, exist_ok=True)
            with open(f"{path_to_save}/{query}.txt", 'w') as f:
                for link in links:
                    if link is not None:
                        f.write(link + '\n')
        else:
            with open(f"{query}.txt", 'w') as f:
                for link in links:
                    if link is not None:
                        f.write(link + '\n')
