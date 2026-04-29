import requests
from lxml import html
import pandas as pd

url  = 'https://keychron.ca/collections/keychron-lemokey-series-keyboard-collection'
response = requests.get(url)
parsed_content = html.fromstring(response.content)

i = 1
j = 1
def name_reviews():
        try:
                while True:
                        name_xpath = '//*[@id="filter-results"]/ul/li[' + str(i) + ']/product-card/div[3]/div[1]/div/p[1]/a'

                        curr_name = parsed_content.xpath(name_xpath)[0].text
                        
                        i = i+1

                        review_xpath = '//*[@id="filter-results"]/ul/li[' + str(j) +']/product-card/div[3]/div[1]/div/div[1]/div[1]'

                        curr_review = parsed_content.xpath(review_xpath)[0].get('aria-label')
                        
                        j = j+1
                        return curr_review, curr_name
        except IndexError as e:
                print(e)
