import queue
import threading
from scrapers_img.img_site_scraper import ImagesFromSiteScraper


class MainScraper:
    def __init__(self):
        self.scraper = ImagesFromSiteScraper()
        self.processed_urls = set()

    def run(self, all_links, query, path):
        num_threads = 10
        work_queue = queue.Queue()

        for url in all_links:
            work_queue.put(url)

        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=self.worker, args=(work_queue, query, path))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    def worker(self, work_queue, query, path):
        while True:
            try:
                url = work_queue.get(timeout=1)
                self.process_url(url, query, path)
            except queue.Empty:
                break
            except Exception as e:
                print(f"Error in worker thread: {e}")

    def process_url(self, url, query, path, timeout=15):
        try:
            if url not in self.processed_urls:
                timer = threading.Timer(timeout, self.handle_timeout, args=(url,))
                timer.start()

                self.scraper.scrape(url)
                self.scraper.save_images(f"{path}/{query}")

                timer.cancel()
                self.processed_urls.add(url)
            else:
                print(f"Skipping duplicate URL: {url}")
        except Exception as e:
            print(f"Error processing {url}: {e}")

    def handle_timeout(self, url):
        print(f"Timeout reached while processing {url}. Skipping to next link.")
