from pathlib import Path
from selenium import webdriver
from process_img.imgs_cleaner import ImagesCleaner
from parsers_search.main_parser import MainParser
from scrapers_img.main_scraper import MainScraper
from cataloging_img.imgs_cataloger import ImagesCataloger


class Main:
    def __init__(self):
        pass

    @staticmethod
    def run():
        query = "Leopard 2"
        n_pages_bing = 25
        n_pages_google = 25
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        driver_google = webdriver.Chrome(options=options)
        driver_bing = webdriver.Chrome(options=options)

        parser = MainParser(query, driver_google, driver_bing, n_pages_google, n_pages_bing)
        all_links = parser.parse(path_to_save='./links')

        main_scraper = MainScraper()
        main_scraper.run(all_links, query)

        directory_path = f'./imgs/{query}'

        cleaner = ImagesCleaner(directory=directory_path,
                                save_deleted=True)
        cleaner.run(find_and_delete_one_color_images=True,
                    delete_small_images=True, min_width=60, min_height=60,
                    delete_duplicates=True,
                    delete_mirror_duplicates_horizontal=True,
                    delete_mirror_duplicates_vertical=True,
                    delete_mirror_duplicates_vertical_horizontal=True)

        imgs_cataloger = ImagesCataloger(directory=directory_path)
        imgs_cataloger.split_images_by_tags_resnet()


if __name__ == '__main__':
    main = Main()
    main.run()

