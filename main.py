from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Set a custom user-agent
options = Options()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0")

driver = webdriver.Firefox(options=options)

# Find elements Exercise
driver.get("https://www.python.org/")

# Locate event elements
event_time_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_name_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# Initialize an empty dictionary to store event information
event_dict = {}


time_list = [time.text for time in event_time_list]
name_list = [name.text for name in event_name_list]

# Add event_item to event_dict using count as the key
for count in range(len(time_list)):
    event_dict[count+1] = {
        "time": time_list[count],
        "name": name_list[count]
    }

print(event_dict)

# Close the driver
driver.quit()
