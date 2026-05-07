import requests
from lxml import html

url = "https://keychron.ca/collections/keychron-lemokey-series-keyboard-collection"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
price_list = []
parsed_content = html.fromstring(response.content)

base_url = "https://keychron.ca"

def return_prices():
    for i in range(14):
        price_xpath = '//*[@id="filter-results"]/ul/li[' + str(i+1) + ']/product-card//span[contains(@class,"price")]//span[last()]'

        price = parsed_content.xpath(price_xpath)

        if not price:
            continue

        product_price = price[0].text_content().strip()

        price_list.append(product_price)

    return(price_list)