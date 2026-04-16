# required libraries
import requests
from lxml import html
import pandas as pd

name_list = []
review_list = []
data = []
link_list = []

# getting the URL
url  = 'https://keychron.ca/collections/keychron-lemokey-series-keyboard-collection'
response = requests.get(url)
headers = {"User-Agent": "Mozilla/5.0"}
parsed_content = html.fromstring(response.content)

i = 1
j = 1
try:
    while True:
        name_xpath = '//*[@id="filter-results"]/ul/li[' + str(i) + ']/product-card/div[3]/div[1]/div/p[1]/a'

        curr_name = parsed_content.xpath(name_xpath)[0].text
        
        name_list.append(curr_name)
        i = i+1

        review_xpath = '//*[@id="filter-results"]/ul/li[' + str(j) +']/product-card/div[3]/div[1]/div/div[1]/div[1]'

        curr_review = parsed_content.xpath(review_xpath)[0].get('aria-label')
        
        review_list.append(curr_review)
        j = j+1
except IndexError as e:
        print(e)

for x in range(14):
    price_xpath = '//*[@id="filter-results"]/ul/li[' + str(x+1) + ']/product-card//span[contains(@class,"price")]//span[last()]'
    link_xpath = '//*[@id="filter-results"]/ul/li[' + str(x+1) + ']//a[contains(@href,"/products/")]'

    price = parsed_content.xpath(price_xpath)

    link = parsed_content.xpath(link_xpath)


    product_price = price[0].text_content().strip()
    product_link = link[0].text_content().strip()

    data.append(product_price)
    link_list.append(product_link)
    


print(link_list)

# final CSV file
c = pd.DataFrame({'name':name_list,
                  'review':review_list,
                  'prices':data,
                  'link':link_list
                 })
print(c.head)