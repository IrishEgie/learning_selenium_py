from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import random

# Add random delays between actions to simulate human behavior
def random_delay():
    time.sleep(random.uniform(2, 5))  # Random delay between 2 to 5 seconds

# Set a custom user-agent
options = Options()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0")

driver = webdriver.Firefox(options=options)

# # item_url = "https://www.lazada.com.ph/products/koorui-24e4-powered-by-hkc-va-panel-1ms-mprt-refresh-rate-100-srgb-fhd-24-koorui-24e3-ips-panel-1ms-refresh-rate-99-srgb-fhd-24-gaming-monitor-i3370587922-s17179786987.html"
# item_url = "https://www.amazon.com/KOORUI-FreeSync-Mountable-1920x1080-DisplayPort/dp/B0BCDD4KTK"
# driver.get(item_url)

# price_php = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(f"The price is {price_php.text}")
# random_delay()

driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)

bug_link = driver.find_element(By.XPATH, value= '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

driver.quit()
