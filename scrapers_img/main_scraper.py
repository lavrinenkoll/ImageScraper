import queue
import threading
from scrapers_img.img_site_scraper import ImagesFromSiteScraper


class MainScraper:
    def __init__(self):
        self.scraper = ImagesFromSiteScraper()
        self.processed_urls = set()  # Track processed URLs

    def run(self, all_links, query):
        num_threads = 10
        work_queue = queue.Queue()

        for url in all_links:
            work_queue.put(url)

        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=self.worker, args=(work_queue, query))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    def worker(self, work_queue, query):
        while True:
            try:
                url = work_queue.get(timeout=1)
                self.process_url(url, query)
            except queue.Empty:
                break
            except Exception as e:
                print(f"Error in worker thread: {e}")

    def process_url(self, url, query):
        try:
            if url not in self.processed_urls:
                self.scraper.scrape(url)
                self.scraper.save_images(f"imgs/{query}")
                self.processed_urls.add(url)
            else:
                print(f"Skipping duplicate URL: {url}")
        except Exception as e:
            print(f"Error processing {url}: {e}")
