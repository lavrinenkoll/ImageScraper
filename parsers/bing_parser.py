from bs4 import BeautifulSoup
from parsers.model_parser import ModelParser


class BingModelParser(ModelParser):
    def parse(self, query, n_pages):
        self.links = []
        query += " -site:*.ru -site:*.by -site:*.рф -site:*.бел"
        for page in range(1, n_pages + 1):
            url = f"https://www.bing.com/search?q={query}&first={(page - 1) * 10}"
            print("Parsing Bing:", url)
            self.driver.get(url)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')

            search = soup.find_all('li', class_='b_algo')
            for item in search:
                link_tag = item.find('a')
                if link_tag:
                    self.links.append(link_tag.get('href'))

        return list(set(self.links))

