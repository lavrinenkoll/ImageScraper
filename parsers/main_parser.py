from concurrent.futures import ThreadPoolExecutor

from parsers.bing_parser import BingModelParser
from parsers.google_parser import GoogleModelParser
from tools.file_manager import FileManager


class MainParser:
    def __init__(self, query, driver_google, driver_bing, n_pages_google=1, n_pages_bing=1):
        self.query = query
        self.driver_google = driver_google
        self.driver_bing = driver_bing
        self.n_pages_google = n_pages_google
        self.n_pages_bing = n_pages_bing
        self.all_links = []

        self.bing_parser = BingModelParser(self.driver_bing)
        self.google_parser = GoogleModelParser(self.driver_google)

        self.file_manager = FileManager()

    def parse(self, path_to_save=None):
        self.all_links = []
        with ThreadPoolExecutor() as executor:
            future_bing = executor.submit(self.parse_bing, self.query, self.driver_bing, self.n_pages_bing)
            future_google = executor.submit(self.parse_google, self.query, self.driver_google, self.n_pages_google)

            try:
                links_bing = future_bing.result()
                links_google = future_google.result()
            except Exception as e:
                print("Parsing interrupted:", e)

            self.all_links = links_bing + links_google
            self.all_links = [link for link in self.all_links if link is not None]
            self.all_links = list(set(self.all_links))

            if path_to_save is not None:
                self.file_manager.save_links_to_file(self.all_links, self.query + " _ sites", path_to_save)

        return self.all_links

    def parse_bing(self, query, driver, n_pages=1):
        self.bing_parser.parse(query, n_pages)
        driver.quit()
        return self.bing_parser.links

    def parse_google(self, query, driver, n_pages=1):
        self.google_parser.parse(query, n_pages)
        driver.quit()
        return self.google_parser.links

