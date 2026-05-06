import requests
from lxml import html
import pandas as pd

url = "https://keychron.ca/collections/keychron-lemokey-series-keyboard-collection"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
price_list = []
parsed_content = html.fromstring(response.content)

base_url = "https://keychron.ca"

def return_colors():
    for i in range(20):
        color_xpath = '//*[@id="filter-results"]/ul/li[' + str(i+1) + ']/product-card/div[3]/div[1]/div/p[2]'
        name_xpath = '/html/body/main/div[3]/div/custom-pagination/div[2]/ul/li[' + str(i+1) + ']/product-card/div[3]/div[1]/div/p[1]/a/text()'
        link_xpath = '//*[@id="filter-results"]/ul/li[' + str(i+1) + ']//a[contains(@href,"/products/")]'

        color = parsed_content.xpath(color_xpath)
        name = parsed_content.xpath(name_xpath)
        link = parsed_content.xpath(link_xpath)

        if not color or not name or not link:
            continue

        product_name = name[0].strip()
        product_color = color[0].text_content().strip()
        product_link = base_url + link[0].get("href")

        price_list.append(product_color)

    print(price_list)


return_colors()