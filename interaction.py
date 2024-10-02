from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0")

driver = webdriver.Firefox(options=options)

# Find elements Exercise
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

# # print(article_count)
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, value="Content Portals")
# all_portals.click()


# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python",Keys.ENTER)

#------------------------------Interaction Challenge-------------------------------------#

driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
submit = driver.find_element(By.CSS_SELECTOR, value="button")


fname.send_keys("Ej", Keys.TAB)
lname.send_keys("Arao", Keys.TAB)
email.send_keys("asdfad@email.com", Keys.TAB)
submit.send_keys(Keys.ENTER)

# # Close the driver
# driver.quit()
