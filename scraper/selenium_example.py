from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# keep browser open
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

# PATH = "C:\Program Files (x86)\chromedriver.exe"
PATH = "/mnt/c/Program Files (x86)/chromedriver.exe"

driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()