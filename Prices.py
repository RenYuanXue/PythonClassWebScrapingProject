import requests
from lxml import html
import pandas as pd

url = "https://keychron.ca/collections/keychron-lemokey-series-keyboard-collection"
headers = {"User-Agent": "Mozilla/5.0"}
data = []
response = requests.get(url, headers=headers)
parsed_content = html.fromstring(response.content)


for i in range(12):
    price_xpath = '//*[@id="filter-results"]/ul/li[' + str(i+1) + ']/product-card//span[contains(@class,"price")]//span[last()]'
    name_xpath = '/html/body/main/div[3]/div/custom-pagination/div[2]/ul/li[' + str(i+1) + ']/product-card/div[3]/div[1]/div/p[1]/a/text()'
    link_xpath = '//*[@id="filter-results"]/ul/li[' + str(i+1) + ']//a[contains(@href,"/products/")]'

    price = parsed_content.xpath(price_xpath)
    name = parsed_content.xpath(name_xpath)
    link = parsed_content.xpath(link_xpath)

    product_name = name[0].strip()
    product_price = price[0].text_content().strip()

    data.append([product_name, product_price])

df = pd.DataFrame(data, columns=["Name", "Price"])
print(df)

df.to_csv("keychron_products.csv", index=False)



