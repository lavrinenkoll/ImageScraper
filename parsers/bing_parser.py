from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from parsers.search_parser import SearchParser


class BingSearchParser(SearchParser):
    def parse(self, query, n_pages):
        self.links = []
        for page in range(1, n_pages + 1):
            url = f"https://www.bing.com/search?q={query}&first={(page - 1) * 10}"
            self.driver.get(url)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')

            search = soup.find_all('li', class_='b_algo')
            for item in search:
                link_tag = item.find('a')
                if link_tag:
                    self.links.append(link_tag.get('href'))

        return list(set(self.links))

