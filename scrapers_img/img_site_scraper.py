import os
from io import BytesIO
import requests
from PIL import Image
from bs4 import BeautifulSoup
from tools.file_manager import FileManager


class ImagesFromSiteScraper:
    def __init__(self):
        self.images = []
        self.file_manager = FileManager()

    def scrape(self, url):
        self.images = []
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.images = soup.find_all('img')

        for i, image in enumerate(self.images):
            try:
                src = image['src']
                if src.startswith('//'):
                    continue
                if not src.startswith('http'):
                    third_slash_index = url.find('/', url.find('/', url.find('/') + 1) + 1)
                    trimmed_url = url[:third_slash_index + 1]
                    image_url = trimmed_url + src[1:]
                    self.images[i]['src'] = image_url

            except Exception as e:
                print("Error" + str(e))

        return self.images

    def save_images(self, path):
        for i, image in enumerate(self.images):
            image_url = image['src']

            if not image_url.startswith('http'):
                continue

            if not image_url.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue

            self.file_manager.save_img_from_url(image_url, path)
