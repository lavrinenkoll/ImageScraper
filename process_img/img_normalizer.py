import queue
import threading

import cv2
import numpy as np
from PIL import Image
from skimage import io
from tools.file_manager import FileManager


class ImagesNormalizer:
    def __init__(self, lightness=True, contrast=True, color=True, sharpness=True):
        self.file_manager = FileManager()
        self.lightness = lightness
        self.contrast = contrast
        self.color = color
        self.sharpness = sharpness

    def normalize_all(self, img):
        try:
            if self.contrast:
                img = self.normalize_contrast(img)
            if self.lightness:
                img = self.normalize_lightness(img)
            if self.color:
                img = self.normalize_color(img)
            if self.sharpness:
                img = self.normalize_sharpness(img)

            return img
        except (IOError, OSError, ValueError) as e:
            print(f"Error processing image: {e}")

    def normalize_images(self, directory):
        work_queue = queue.Queue()

        for image_file in self.file_manager.get_image_files(directory):
            work_queue.put(image_file)

        threads = []
        num_threads = 10
        for _ in range(num_threads):
            thread = threading.Thread(target=self.worker, args=(work_queue,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    def worker(self, work_queue):
        while not work_queue.empty():
            try:
                image_file = work_queue.get_nowait()
                self.process_image(image_file)
            except queue.Empty:
                break

    def process_image(self, image_file):
        try:
            img = io.imread(image_file)
            print(f"Normalizing {image_file}")
            normalized_img = self.normalize_all(img)
            img = Image.fromarray(np.uint8(normalized_img))
            img.save(image_file)
        except (IOError, OSError, ValueError) as e:
            print(f"Error processing {image_file}: {e}")

    @staticmethod
    def normalize_lightness(img):
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])
        normalized_img = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

        return normalized_img

    @staticmethod
    def normalize_contrast(img):
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l_channel, a_channel, b_channel = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(4, 4))
        l_channel = clahe.apply(l_channel)
        lab = cv2.merge((l_channel, a_channel, b_channel))
        normalized_img = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

        return normalized_img

    @staticmethod
    def normalize_color(img):
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
        normalized_img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

        return normalized_img

    @staticmethod
    def normalize_sharpness(img):
        blurred = cv2.GaussianBlur(img, (0, 0), 3)
        normalized_img = cv2.addWeighted(img, 1.5, blurred, -0.5, 0)

        return normalized_img
