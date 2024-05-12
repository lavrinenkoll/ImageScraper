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
        query = "Leopard 2 tank photos"
        n_pages_bing = 5
        n_pages_google = 5
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        # driver_google = webdriver.Chrome(options=options)
        # driver_bing = webdriver.Chrome(options=options)
        #
        # parser = MainParser(query, driver_google, driver_bing, n_pages_google, n_pages_bing)
        # all_links = parser.parse(path_to_save='./links')
        #
        # main_scraper = MainScraper()
        # main_scraper.run(all_links, query)

        directory_path = f'./imgs/{query}'
        count_before_cleaning = (len(list(Path(directory_path).rglob('*')))
                                 - 1 - len(list(Path(directory_path+"/deleted").rglob('*.txt'))))

        cleaner = ImagesCleaner(directory=directory_path,
                                save_deleted=True)

        cleaner.run(find_and_delete_trash_images=True, white_images=True, black_images=True,
                    delete_small_images=True, min_width=60, min_height=60,
                    delete_duplicates=True,
                    delete_mirror_duplicates_horizontal=True,
                    delete_mirror_duplicates_vertical=True,
                    delete_mirror_duplicates_vertical_horizontal=True)

        cleaner.get_image_files()
        count_after_cleaning = len(list(Path(directory_path).rglob('*')))
        print(f"Number of images before cleaning: {count_before_cleaning}")
        print(f"Number of images after cleaning: {count_after_cleaning}")


if __name__ == '__main__':
    main = Main()
    main.run()

