from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0")

driver = webdriver.Firefox(options=options)

# Find elements Exercise
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

# # print(article_count)
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, value="Content Portals")
# all_portals.click()


search = driver.find_element(By.NAME, value="search")
search.send_keys("Python",Keys.ENTER)


# # Close the driver
# driver.quit()
