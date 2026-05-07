import requests
from lxml import html

url = "https://keychron.ca/collections/keychron-lemokey-series-keyboard-collection"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
color_list = []
parsed_content = html.fromstring(response.content)

base_url = "https://keychron.ca"

def return_colors():
    for i in range(14):
        color_xpath = '//*[@id="filter-results"]/ul/li[' + str(i+1) + ']/product-card/div[3]/div[1]/div/p[2]'

        color = parsed_content.xpath(color_xpath)

        if not color:
            color_list.append("N/A")
            continue

        product_color = color[0].text_content().strip()

        color_list.append(product_color)

    return(color_list)