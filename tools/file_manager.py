import os
import shutil
import time


class FileManager:
    def __init__(self, directory):
        self.directory = directory
        self.extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')

    def delete_file(self, file_path, max_retries=3, retry_delay=1, save_deleted=False):
        retries = 0
        while retries < max_retries:
            try:
                if os.path.exists(file_path):

                    if save_deleted:
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

    def get_image_files(self):
        image_files = []
        try:
            for file in os.listdir(self.directory):
                if file.endswith(self.extensions):
                    image_files.append(os.path.join(self.directory, file))
        except OSError as e:
            print(f"Error listing files in {self.directory}: {e}")
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
    def move_files_to_folders(folder_files_map):
        for folder, files in folder_files_map.items():
            os.makedirs(folder, exist_ok=True)
            for file in files:
                try:
                    shutil.move(file, folder)
                except Exception as e:
                    continue
