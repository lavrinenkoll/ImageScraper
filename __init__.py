from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from selenium import webdriver
from parsers_search.bing_parser import BingSearchParser
from parsers_search.google_parser import GoogleSearchParser

def parse_bing(query, driver, n_pages=3):
    parser = BingSearchParser(driver)
    parser.parse(query, n_pages)
    driver.quit()
    return parser.links


def parse_google(query, driver, n_pages=3):
    parser = GoogleSearchParser(driver)
    parser.parse(query, n_pages)
    driver.quit()
    return parser.links


query = "Leopard 2"
n_pages_bing = 10
n_pages_google = 10
driver_google = webdriver.Chrome()
driver_bing = webdriver.Chrome()


with ThreadPoolExecutor() as executor:
    future_bing = executor.submit(parse_bing, query, driver_bing, n_pages_bing)
    future_google = executor.submit(parse_google, query, driver_google, n_pages_google)

    links_bing = future_bing.result()
    links_google = future_google.result()


print("Bing Links:", links_bing)
print("Number of Bing Links:", len(links_bing))
print("Google Links:", links_google)
print("Number of Google Links:", len(links_google))

all_links = links_bing + links_google
all_links = [link for link in all_links if link is not None]
all_links = list(set(all_links))

with open(f"{query}.txt", 'w') as f:
    for link in all_links:
        if link is not None:
            f.write(link + '\n')



# def get_images(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     images = soup.find_all('img')
#
#     for i, image in enumerate(images):
#         src = image['src']
#         if src.startswith('//'):
#             continue
#         if not src.startswith('http'):
#             third_slash_index = url.find('/', url.find('/', url.find('/') + 1) + 1)
#             trimmed_url = url[:third_slash_index + 1]
#             image_url = trimmed_url + src[1:]
#             images[i]['src'] = image_url
#     return images
#
#
# def save_images(images):
#     for i, image in enumerate(images):
#         image_url = image['src']
#
#         if not image_url.startswith('http'):
#             continue
#
#         if not image_url.lower().endswith(('.jpg', '.jpeg', '.png')):
#             continue
#
#         try:
#             response = requests.get(image_url)
#             img = Image.open(BytesIO(response.content))
#             # Save image to file with a unique name based on index and image source URL
#             # create folder
#             Path(f"imgs/{query}").mkdir(parents=True, exist_ok=True)
#             img.save(f"imgs/{query}/{i}_{image_url.split('/')[-1]}")
#             print(f"Succesfully processed image {image_url}")
#         except Exception as e:
#             print(f"Error processing image {image_url}: {e}")
#
#
# for url in all_links:
#     try:
#         images = get_images(url)
#         save_images(images)
#     except Exception as e:
#         print(f"Error processing {url}: {e}")


from scrapers_img.img_site_scraper import ImagesFromSiteScraper

scraper = ImagesFromSiteScraper()

for url in all_links:
    try:
        scraper.scrape(url)
        images = scraper.images
        scraper.save_images(Path("imgs"), query)
    except Exception as e:
        print(f"Error processing {url}: {e}")
