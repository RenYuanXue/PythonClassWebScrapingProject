import requests
from lxml import html
import pandas as pd

name_list = []
review_list = []
url  = 'https://keychron.ca/collections/keychron-lemokey-series-keyboard-collection'
response = requests.get(url)
parsed_content = html.fromstring(response.content)


def name_reviews():
        try:
            i = 1
            j = 1
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
        return review_list, name_list
