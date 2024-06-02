# selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
# Importante 
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-default-apps")
chrome_options.add_argument("--disable-translate")
chrome_options.add_argument("--disable-web-security")  
chrome_options.add_argument("--ignore-certificate-errors")

web_url = 'https://www.amazon.com/s?rh=n%3A565108&fs=true&language=es&ref=lp_565108_sar'

driver = webdriver.Chrome(options=chrome_options)
driver.get(web_url)
import time
time.sleep(5)
html = driver.page_source
with open('products_amazon.html', 'w', encoding='utf-8') as f:
    f.write(html)
driver.quit()


from bs4 import BeautifulSoup

with open('products_amazon.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
sg_col_inner_class_list = soup.find_all('div', class_='sg-col-inner')
products = []
page_number = 1
for idx, sg_col_inner in enumerate(sg_col_inner_class_list):
    images = sg_col_inner.find_all('img')
    product_image = images[0]['src'] if images else None
    h2s = sg_col_inner.find_all('h2')
    product_name = h2s[0].text if h2s else None
    alinks = sg_col_inner.find_all('a')
    product_link = alinks[0]['href'] if alinks else None
    span_class_reviews = sg_col_inner.find_all('span', class_='a-size-base')
    product_review = span_class_reviews[0].text if span_class_reviews else None
    span_price_symbol = sg_col_inner.find_all('span', class_='a-price-symbol')
    product_price_symbol = span_price_symbol[0].text if span_price_symbol else None
    span_price_whole = sg_col_inner.find_all('span', class_='a-price-whole')
    product_price_whole = span_price_whole[0].text if span_price_whole else None
    span_price_fraction = sg_col_inner.find_all('span', class_='a-price-fraction')
    product_price_fraction = span_price_fraction[0].text if span_price_fraction else None
    div_extra_message = sg_col_inner.find_all('div', class_='a-row a-size-base a-color-secondary')
    product_extra_message = div_extra_message[0].text if div_extra_message else None
    product_extra_links = div_extra_message[0].find_all('a') if div_extra_message else None
    product_extra_link = product_extra_links[0]['href'] if product_extra_links else None

    if product_image is None:
        continue
    
    products.append(
        {
            'page_number': page_number,
            'product_number': idx + 1,
            'product_image': product_image,
            'product_name': product_name,
            'product_link': product_link,
            'product_review': product_review,
            'product_price_symbol': product_price_symbol,
            'product_price_whole': product_price_whole,
            'product_price_fraction': product_price_fraction,
            'product_extra_message': product_extra_message,
            'product_extra_link': product_extra_link
        }
    )

import json
with open('products_amazon.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=4)