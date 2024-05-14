import time
from selenium import webdriver

from process_img.imgs_cleaner import ImagesCleaner
from parsers.main_parser import MainParser
from scrapers_img.main_scraper import MainScraper
from cataloging_img.imgs_cataloger import ImagesCataloger


class Main:
    def __init__(self):
        pass

    @staticmethod
    def run():
        str_result = ""

        query = "top cat breeds"
        n_pages_bing = 30
        n_pages_google = 30
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        driver_google = webdriver.Chrome(options=options)
        driver_bing = webdriver.Chrome(options=options)

        time_start = time.time()
        parser = MainParser(query, driver_google, driver_bing, n_pages_google, n_pages_bing)
        all_links = parser.parse(path_to_save='./links')
        time_end = time.time()
        str_result += f"Time spent on parsing: {time_end - time_start} seconds\n"

        time_start = time.time()
        main_scraper = MainScraper()
        main_scraper.run(all_links, query)
        time_end = time.time()
        str_result += f"Time spent on scraping: {time_end - time_start} seconds\n"

        directory_path = f'C:\Workspace\diplom\parser\imgs/{query}'

        time_start = time.time()
        cleaner = ImagesCleaner(directory=directory_path,
                                save_deleted=True)
        cleaner.run(
                    find_and_delete_one_color_images=True,
                    delete_small_images=True, min_width=100, min_height=100,
                    delete_duplicates=True,
                    delete_mirror_duplicates_horizontal=True,
                    delete_mirror_duplicates_vertical=True,
                    delete_mirror_duplicates_vertical_horizontal=True
                    )
        time_end = time.time()
        str_result += f"Time spent on cleaning: {time_end - time_start} seconds\n"

        # time_start = time.time()
        # imgs_normalizer = ImagesNormalizer(lightness=True, contrast=True, color=True, sharpness=True)
        # imgs_normalizer.normalize_images(directory_path)
        # time_end = time.time()
        # str_result += f"Time spent on normalizing: {time_end - time_start} seconds\n"

        # time_start = time.time()
        # imgs_cataloger = ImagesCataloger(directory=directory_path)
        # imgs_cataloger.split_images_by_tags_resnet()
        # time_end = time.time()
        # str_result += f"Time spent on cataloging: {time_end - time_start} seconds\n"

        time_start = time.time()
        imgs_cataloger = ImagesCataloger(directory=directory_path)
        imgs_cataloger.split_images_by_resolution_auto()
        time_end = time.time()
        str_result += f"Time spent on cataloging: {time_end - time_start} seconds\n"

        print(str_result)


if __name__ == '__main__':
    main = Main()
    main.run()

