from bs4 import BeautifulSoup
from parsers_search.search_parser import SearchParser


class GoogleSearchParser(SearchParser):
    def parse(self, query, n_pages):
        self.links = []
        for page in range(1, n_pages+1):
            url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 10)
            self.driver.get(url)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            # soup = BeautifulSoup(r.text, 'html.parser')

            search = soup.find_all('div', class_="yuRUbf")
            for h in search:
                self.links.append(h.a.get('href'))

        return list(set(self.links))


