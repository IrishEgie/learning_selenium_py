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
event_elements = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul').text
event_list = event_elements.split("\n")

# Initialize an empty dictionary to store event information
event_dict = {}
count = 0

# Loop through the event list and extract dates and event names
for i in range(0, len(event_list), 2):
    event_tag = {}
    event_tag['time'] = event_list[i]  # Date
    event_tag['name'] = event_list[i+1]  # Event name
    
    count += 1
    event_dict[f'{count}'] = event_tag

# Print the final dictionary
print(event_dict)

# Close the driver
driver.quit()
