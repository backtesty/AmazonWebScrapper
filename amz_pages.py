

# href="/-/es/s?i=computers&rh=n%3A565108&fs=true&language=es&qid=1718379581&ref=sr_pg_1"


# href="/-/es/s?i=computers&rh=n%3A565108&fs=true&page=2&language=es&qid=1718379581&ref=sr_pg_2"
# href="/-/es/s?i=computers&rh=n%3A565108&fs=true&page=4&language=es&qid=1718379581&ref=sr_pg_4"

# https://www.amazon.com/-/es/s?i=computers&rh=n%3A565108&fs=true&page=3&language=es&qid=1718379576&ref=sr_pg_3

import time, random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox") # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage") # Overcome limited resource problems
chrome_options.add_argument("--disable-gpu") # applicable to windows os only
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")

computers = []
url_base = "https://www.amazon.com/-/es/s?"
for page in range(1, 4): # 401
    url_page = f'{url_base}i=computers&rh=n%3A565108&fs=true&page={page}&language=es&qid=1718379581&ref=sr_pg_{page}'
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url_page)
    time_random = random.randint(5, 10)
    time.sleep(time_random)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()
    sg_col_inner_list = soup.find_all('div', class_='sg-col-inner')
    for index, product in enumerate(sg_col_inner_list):
        images = product.find_all('img')
        product_image = images[0]['src'] if images else None
        h2s = product.find_all('h2')
        product_name = h2s[0].text if h2s else None
        alinks = product.find_all('a')
        product_link = alinks[0]['href'] if alinks else None
        span_price_whole = product.find_all('span', class_='a-price-whole')
        product_price = span_price_whole[0].text if span_price_whole else None
        span_price_fraction = product.find_all('span', class_='a-price-fraction')
        product_price_fraction = span_price_fraction[0].text if span_price_fraction else None

        if product_image is None:
            continue

        computers.append({
            'index': index,
            'page_number': page,
            'product_name': product_name,
            'product_image': product_image,
            'product_link': product_link,
            'product_price': product_price,
            'product_price_fraction': product_price_fraction
        })

import json
with open('computers.json', 'w', encoding='utf-8') as file:
    json.dump(computers, file, ensure_ascii=False, indent=4)
        