import os
import shutil
from collections import defaultdict
from random import random

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

    def calculate_resolutions(self, max_clusters=10):
        self.image_files = self.file_manager.get_image_files()
        sizes = []

        for image_file in self.image_files:
            try:
                with Image.open(image_file) as img:
                    width, height = img.size
                    sizes.append((width, height))
            except (IOError, OSError, ValueError) as e:
                print(f"Error processing {image_file}: {e}")

        sizes_array = np.array(sizes)

        best_silhouette_score = -1
        optimal_num_clusters = 2
        for num_clusters in range(3, max_clusters + 1):
            kmeans = KMeans(n_clusters=num_clusters, random_state=42)
            cluster_labels = kmeans.fit_predict(sizes_array)
            silhouette_avg = silhouette_score(sizes_array, cluster_labels)

            if silhouette_avg > best_silhouette_score:
                best_silhouette_score = silhouette_avg
                optimal_num_clusters = num_clusters

        kmeans = KMeans(n_clusters=optimal_num_clusters, random_state=42)
        cluster_labels = kmeans.fit_predict(sizes_array)
        clusters = [[] for _ in range(optimal_num_clusters)]

        for i, label in enumerate(cluster_labels):
            clusters[label].append(sizes[i])

        list_resolutions = []
        for cluster in clusters:
            cluster = np.array(cluster)
            min_width, min_height = np.min(cluster, axis=0)
            max_width, max_height = np.max(cluster, axis=0)
            list_resolutions.append(((min_width, min_height), (max_width, max_height)))

        list_resolutions = sorted(list_resolutions, key=lambda x: x[0][0])

        # plt.figure(figsize=(15, 10))
        # plt.scatter(*zip(*sizes))
        # plt.xlabel('Width')
        # plt.ylabel('Height')
        # plt.title('Image sizes')
        # for resolution in list_resolutions:
        #     min_width, min_height = resolution[0]
        #     max_width, max_height = resolution[1]
        #     color = (random(), random(), random())
        #     plt.fill_between([min_width, max_width], min_height, max_height, color=color, alpha=0.2)
        # plt.show()

        return list_resolutions

    def split_images_by_resolution_auto(self, max_clusters=10):
        resolutions = self.calculate_resolutions(max_clusters)
        self.split_images_by_resolution(resolutions)

    def split_images_by_file_size(self, list_file_sizes):
        self.image_files = self.file_manager.get_image_files()

        if type(list_file_sizes[0][0]) is str:
            list_file_sizes = [(self.get_file_size_from_text(file_size[0]), self.get_file_size_from_text(file_size[1]))
                               for file_size in list_file_sizes]

        for file_size in list_file_sizes:
            min_size, max_size = file_size
            folder_name = f"{self.parse_file_size(min_size)}_{self.parse_file_size(max_size)}"
            folder_path = os.path.join(self.directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            files_to_move = []

            for image_file in self.image_files:
                try:
                    if min_size <= os.path.getsize(image_file) <= max_size:
                        files_to_move.append(image_file)
                except Exception as e:
                    print(f"Error processing {image_file}: {e}")

            for image_file in files_to_move:
                try:
                    shutil.move(image_file, folder_path)
                except Exception as e:
                    print(f"Error moving {image_file} to {folder_path}: {e}")

            self.image_files = [f for f in self.image_files if f not in files_to_move]

    def calculate_file_sizes(self, max_clusters=10):
        self.image_files = self.file_manager.get_image_files()
        file_sizes = []

        for image_file in self.image_files:
            try:
                file_size = os.path.getsize(image_file)
                file_sizes.append(file_size)
            except Exception as e:
                print(f"Error processing {image_file}: {e}")

        file_sizes_array = np.array(file_sizes).reshape(-1, 1)

        best_silhouette_score = -1
        optimal_num_clusters = 2
        for num_clusters in range(3, max_clusters + 1):
            kmeans = KMeans(n_clusters=num_clusters, random_state=42)
            cluster_labels = kmeans.fit_predict(file_sizes_array)
            silhouette_avg = silhouette_score(file_sizes_array, cluster_labels)

            if silhouette_avg > best_silhouette_score:
                best_silhouette_score = silhouette_avg
                optimal_num_clusters = num_clusters

        kmeans = KMeans(n_clusters=optimal_num_clusters, random_state=42)
        cluster_labels = kmeans.fit_predict(file_sizes_array)
        clusters = defaultdict(list)

        for i, label in enumerate(cluster_labels):
            clusters[label].append(file_sizes[i])

        list_file_sizes = []
        for cluster in clusters.values():
            cluster = np.array(cluster)
            min_size = np.min(cluster)
            max_size = np.max(cluster)
            list_file_sizes.append((min_size, max_size))

        list_file_sizes = sorted(list_file_sizes, key=lambda x: x[0])

        # plt.figure(figsize=(15, 10))
        # plt.scatter(range(len(file_sizes)), file_sizes)
        # plt.xlabel('Image')
        # plt.ylabel('File size')
        # plt.title('Image file sizes')
        # for file_size in list_file_sizes:
        #     min_size, max_size = file_size
        #     color = (random(), random(), random())
        #     plt.fill_between(range(len(file_sizes)), min_size, max_size, color=color, alpha=0.2)
        # plt.show()

        return list_file_sizes

    def split_images_by_file_size_auto(self, max_clusters=10):
        file_sizes = self.calculate_file_sizes(max_clusters)
        self.split_images_by_file_size(file_sizes)

    @staticmethod
    def parse_file_size(file_size):
        if file_size < 1024:
            return f"{file_size}B"
        elif file_size < 1024 ** 2:
            return f"{file_size / 1024:.2f}KB"
        elif file_size < 1024 ** 3:
            return f"{file_size / 1024 ** 2:.2f}MB"
        else:
            return f"{file_size / 1024 ** 3:.2f}GB"

    @staticmethod
    def get_file_size_from_text(file_size_text):
        if file_size_text[-2:] == 'GB':
            return float(file_size_text[:-2]) * 1024 ** 3
        elif file_size_text[-2:] == 'MB':
            return float(file_size_text[:-2]) * 1024 ** 2
        elif file_size_text[-2:] == 'KB':
            return float(file_size_text[:-2]) * 1024
        elif file_size_text[-1] == 'B':
            return float(file_size_text[:-1])



path = '../imgs/Leopard 2 — копия (2)'
#path = '../imgs/Leopard 2 tank photos'
#path = '../imgs/Leopard 2 tank — копия'
img_cataloger = ImageCataloger(directory=path)

img_cataloger.extract_images_from_folders()
#
# img_cataloger.split_images_by_resolution(list_resolutions=[((150, 150), (600, 600)), ((600, 600), (1500, 1500))])
#img_cataloger.split_images_by_file_size(list_file_sizes=[('10B', '100KB'), ('100KB', '500KB'), ('500KB', '1MB')])

#img_cataloger.split_images_by_resolution_auto(max_clusters=15)
img_cataloger.split_images_by_file_size_auto(max_clusters=15)


