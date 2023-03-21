from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import requests
import itertools
from bs4 import BeautifulSoup

# CHROMEDRIVER_PATH = "/mnt/c/Program Files (x86)/chromedriver.exe"
FIREFOX_DRIVER_PATH = "/mnt/c/Program Files (x86)/geckodriver.exe"
FIREFOX_OPTIONS = Options()
FIREFOX_OPTIONS.headless = True
# FIREFOX_OPTIONS.add_experimental_option('detach', True)
# CHROME_OPTIONS.headless = True
WEBDRIVER = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH, options=FIREFOX_OPTIONS)
kirkland_signature_page_prefix = list('https://www.costco.ca/kirkland-signature-products.html?currentPage=')
kirkland_signature_page_postfix = list('&pageSize=24')

# start at this page, get all product links on current page and save
# if the next button exists, click it
# go to first step

def get_product_price_and_name(product_soup):
    '''
    returns the name and price of the product
    '''
    # just print html for now as soup
    # print(type(product_soup))
    product_price = product_soup.find('div', 'price').text
    product_name = product_soup.find('span', {'class': 'description'}).text
    return {
        'name': product_name.strip(),
        'price': product_price.strip()
    }



def get_product_links_on_current_page():
    '''
    given html page for costco, find all product links on the current page
    '''
    # driver = WEBDRIVER
    current_page_num = 1
    all_product_mapping = dict()
    while current_page_num < 10:
        # increment 67th char which is the current page number
        # kirkland_signature_page[67] = str(current_page_num)
        str_kirkland_signature_page = ''.join(itertools.chain(kirkland_signature_page_prefix, str(current_page_num), kirkland_signature_page_postfix))
        # print('asdlfkjbawlieug')
        # webpage = requests.get(str_kirkland_signature_page)
        # print('awelkfuawe')
        WEBDRIVER.get(str_kirkland_signature_page)
        page_source = WEBDRIVER.page_source
        # print(a)
        soup = BeautifulSoup(page_source, 'html.parser')
        # product_grid = soup.find('div', {'class': 'product-list grid'})
        # product_grid = soup.find_all('span', 'description')
        # product_grid = soup.find_all('div', 'thumbnail')
        product_grid = soup.find_all('div', 'caption link-behavior')

        if len(product_grid) == 0:
            break

        for product_html in product_grid:
            cur_product_details = get_product_price_and_name(product_html)
            # print(cur_product_details)
            # print(product_html)
            # break
            all_product_mapping[cur_product_details['name']] = cur_product_details['price']
        current_page_num += 1
        # if current_page_num > 9:
        #     break
    # print(str_kirkland_signature_page)
    print(all_product_mapping)
    WEBDRIVER.quit()
        # print(webpage)
        # try:
        #     kirkland_signature_page[67] = str(current_page_num)
        #     webpage = requests.get(str(kirkland_signature_page)).content
        #     # print(webpage)
        #     print(current_page_num)
        # except:
        #     print('something happened!')
        #     break
        # driver.get(kirkland_signature_page)
        # webpage = driver.page_source
        # print(webpage)

get_product_links_on_current_page()
# exit(0)
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',}
# requests.get('https://www.costco.ca/kirkland-signature-products.html?currentPage=1&pageSize=24', timeout=5, headers=headers)
# requests.get('https://www.costco.ca/', timeout=5, headers=headers)
# WEBDRIVER.get('https://www.costco.ca/kirkland-signature-products.html?currentPage=1&pageSize=24')
# a = WEBDRIVER.page_source
# WEBDRIVER.quit()
# # print(a)
# soup = BeautifulSoup(a, 'html.parser')
# # product_grid = soup.find('div', {'class': 'product-list grid'})
# # product_grid = soup.find_all('span', 'description')
# # product_grid = soup.find_all('div', 'thumbnail')
# product_grid = soup.find_all('div', 'caption link-behavior')
# all_product_mapping = dict()
# for product_html in product_grid:
#     cur_product_details = get_product_price_and_name(product_html)
#     # print(cur_product_details)
#     # print(product_html)
#     # break
#     all_product_mapping[cur_product_details['name']] = cur_product_details['price']
# print(all_product_mapping)
    
    

# print(product_grid)
