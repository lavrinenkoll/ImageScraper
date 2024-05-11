from pathlib import Path
from selenium import webdriver
from process_img.imgs_cleaner import ImagesCleaner
from parsers_search.main_parser import MainParser
from scrapers_img.main_scraper import MainScraper

query = "Leopard 2"
n_pages_bing = 5
n_pages_google = 5
driver_google = webdriver.Chrome()
driver_bing = webdriver.Chrome()

parser = MainParser(query, driver_google, driver_bing, n_pages_google, n_pages_bing)
all_links = parser.parse()

main_scraper = MainScraper(all_links, query)
main_scraper.run()

directory_path = f'./imgs/{query}'
count_before_cleaning = len(list(Path(directory_path).rglob('*')))

cleaner = ImagesCleaner(directory_path)
cleaner.run()

cleaner.get_image_files()
count_after_cleaning = len(list(Path(directory_path).rglob('*')))
print(f"Number of images before cleaning: {count_before_cleaning}")
print(f"Number of images after cleaning: {count_after_cleaning}")
