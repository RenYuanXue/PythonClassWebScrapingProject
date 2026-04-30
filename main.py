from lxml import html
import lxml
import requests

url = "https://keychron.ca/collections/keychron-lemokey-series-keyboard-collection"
response = requests.get(url)

parsed_content = html.fromstring(response.content)

for i in range(14):
    item_xpath = '//*[@id="shopify-section-template--26044941336941__collection-banner"]/div/div/div/div[1]/h1['+ str(i+1) + ']/div/div[2]/div/p[2]'
    section_xpath = '//*[@id="filter-results"]/ul/li[2]['+ str(i+1) + ']/div/div[2]/div/p[1]/strong'
    hyperlink_xpath = '//*[@id="filter-results"]/ul/li[2]['+ str(i+1) + ']'
    
    curr_item = parsed_content.xpath(item_xpath)[0].text
    curr_section = parsed_content.xpath(section_xpath)[0].text
    hyperlink_xpath = parsed_content.xpath(hyperlink_xpath)[0].get('href')

    print(curr_section)
    print(curr_item)
    print('https://keychron.ca/collections/keychron-lemokey-series-keyboard-collection' + hyperlink_xpath)
    print()