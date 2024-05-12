from pathlib import Path
from selenium import webdriver
from process_img.imgs_cleaner import ImagesCleaner
from parsers_search.main_parser import MainParser
from scrapers_img.main_scraper import MainScraper


class Main:
    def __init__(self):
        pass

    @staticmethod
    def run():
        query = ("Leopard 2 tank")
        n_pages_bing = 1
        n_pages_google = 1
        driver_google = webdriver.Chrome()
        driver_bing = webdriver.Chrome()

        parser = MainParser(query, driver_google, driver_bing, n_pages_google, n_pages_bing)
        all_links = parser.parse(path_to_save='./links')

        main_scraper = MainScraper(all_links, query)
        main_scraper.run()

        directory_path = f'./imgs/{query}'
        count_before_cleaning = (len(list(Path(directory_path).rglob('*')))
                                 - 1 - len(list(Path(directory_path+"/deleted").rglob('*.txt'))))

        cleaner = ImagesCleaner(directory=directory_path,
                                save_deleted=True)

        cleaner.run(delete_small_images=True,
                    min_width=60,
                    min_height=60,
                    delete_duplicates=True,
                    delete_mirror_duplicates_horizontal=True,
                    delete_mirror_duplicates_vertical=True)

        cleaner.get_image_files()
        count_after_cleaning = len(list(Path(directory_path).rglob('*')))
        print(f"Number of images before cleaning: {count_before_cleaning}")
        print(f"Number of images after cleaning: {count_after_cleaning}")


if __name__ == '__main__':
    main = Main()
    main.run()

