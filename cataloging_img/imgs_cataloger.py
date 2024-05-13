import os
import shutil
from collections import defaultdict

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from tools.file_manager import FileManager


class ImageCataloger:
    def __init__(self, directory):
        self.directory = directory
        self.extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')
        self.file_manager = FileManager(directory)
        self.image_files = self.file_manager.get_image_files()

    # def get_image_files(self):
    #     image_files = []
    #     try:
    #         for file in os.listdir(self.directory):
    #             if file.endswith(self.extensions):
    #                 image_files.append(os.path.join(self.directory, file))
    #     except OSError as e:
    #         print(f"Error listing files in {self.directory}: {e}")
    #     if not image_files:
    #         print(f"No images found in {self.directory}")
    #     return image_files

    # def extract_images_from_folders(self, directory):
    #     subdirectories = [os.path.join(directory, d) for d in os.listdir(directory) if
    #                       os.path.isdir(os.path.join(directory, d))]
    #
    #     for subdir in subdirectories:
    #         for file in os.listdir(subdir):
    #             if file.endswith(self.extensions):
    #                 source_path = os.path.join(subdir, file)
    #                 destination_path = os.path.join(directory, file)
    #
    #                 shutil.move(source_path, destination_path)
    #
    #         if not os.listdir(subdir):
    #             os.rmdir(subdir)
    def extract_images_from_folders(self):
        self.file_manager.extract_images_from_folders(self.directory)
        self.image_files = self.file_manager.get_image_files()

    def split_images_by_resolution(self, list_resolutions):
        self.image_files = self.file_manager.get_image_files()

        for resolution in list_resolutions:
            min_width, min_height = resolution[0]
            max_width, max_height = resolution[1]

            folder_name = f"{min_width}x{min_height}_{max_width}x{max_height}"
            folder_path = os.path.join(self.directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            files_to_move = []

            for image_file in self.image_files:
                try:
                    with Image.open(image_file) as img:
                        width, height = img.size
                        if (min_width <= width <= max_width) and (min_height <= height <= max_height):
                            files_to_move.append(image_file)
                except (IOError, OSError, ValueError) as e:
                    print(f"Error processing {image_file}: {e}")

            for image_file in files_to_move:
                try:
                    shutil.move(image_file, folder_path)
                except Exception as e:
                    print(f"Error moving {image_file} to {folder_path}: {e}")

            self.image_files = [f for f in self.image_files if f not in files_to_move]

    def calculate_resolutions(self):
        self.image_files = self.file_manager.get_image_files()
        sizes = []

        for image_file in self.image_files:
            try:
                with Image.open(image_file) as img:
                    width, height = img.size
                    sizes.append((width, height))
            except (IOError, OSError, ValueError) as e:
                print(f"Error processing {image_file}: {e}")

        plt.figure(figsize=(15, 10))
        plt.scatter(*zip(*sizes))
        plt.xlabel('Width')
        plt.ylabel('Height')
        plt.title('Image sizes')
        plt.show()

        sizes_array = np.array(sizes)
        num_clusters = 4
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        kmeans.fit(sizes_array)
        cluster_labels = kmeans.labels_
        clusters = [[] for _ in range(num_clusters)]

        for i, label in enumerate(cluster_labels):
            clusters[label].append(sizes[i])

        list_resolutions = []
        for cluster in clusters:
            cluster = np.array(cluster)
            min_width, min_height = np.min(cluster, axis=0)
            max_width, max_height = np.max(cluster, axis=0)
            list_resolutions.append(((min_width, min_height), (max_width, max_height)))

        list_resolutions = sorted(list_resolutions, key=lambda x: x[0][0])

        return list_resolutions

    def split_images_by_resolution_auto(self):
        resolutions = self.calculate_resolutions()
        self.split_images_by_resolution(resolutions)




path = '../imgs/Leopard 2 — копия (2)'
img_cataloger = ImageCataloger(directory=path)

img_cataloger.extract_images_from_folders()
#
# img_cataloger.split_images_by_resolution(list_resolutions=[((150, 150), (600, 600)), ((600, 600), (1500, 1500))])

img_cataloger.split_images_by_resolution_auto()


