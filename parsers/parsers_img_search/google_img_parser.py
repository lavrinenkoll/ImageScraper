from telnetlib import EC

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait

from parsers.model_parser import ModelParser


class GoogleImageParser(ModelParser):
    def parse_one_url(self, url):
        self.driver.get(url)

        wait.WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, '.czzyk.XOEbc'))

        search_results = self.driver.find_elements(By.CSS_SELECTOR, '.czzyk.XOEbc')
        current_window_handle = self.driver.current_window_handle

        for item in search_results:
            try:
                action = ActionChains(self.driver)
                action.key_down(Keys.CONTROL).click(item).key_up(Keys.CONTROL).perform()

                self.driver.switch_to.window(self.driver.window_handles[-1])

                self.links.append(self.driver.current_url)

                self.driver.close()

                self.driver.switch_to.window(current_window_handle)
            except Exception as e:
                print("Error:", e)
                continue

    def parse(self, query, n_pages):
        urls = [f"https://www.google.com/search?q={query}&tbm=isch&start={(page - 1) * 100}" for page in
                range(1, n_pages + 1)]

        for url in urls:
            self.parse_one_url(url)

        unique_links = list(set(self.links))
        print("Links:", unique_links)
        return unique_links

