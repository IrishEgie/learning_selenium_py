from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Configure options for the browser
options = Options()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0")

driver = webdriver.Firefox(options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Fetch the web elements for cookie clicking and store items
click_cookie = driver.find_element(By.CSS_SELECTOR, value='div #cookie')

# Function to fetch current money and convert to an integer
def get_current_money():
    money = driver.find_element(By.CSS_SELECTOR, value="div #money").text.replace(",", "")
    if money.isdigit():
        return int(money)
    return 0

# Function to fetch available store items and their costs
def get_store_items():
    store_elem_list = driver.find_elements(By.CSS_SELECTOR, value="div #rightPanel #store div")
    store_elem_cost_list = driver.find_elements(By.CSS_SELECTOR, value="div #rightPanel #store div b")
    store_items = []
    
    for i in range(len(store_elem_cost_list) - 1):
        try:
            store_item_name = store_elem_list[i].text.split(" - ")[0]
            store_item_cost = int(store_elem_cost_list[i].text.split(" - ")[1].replace(",", ""))
            store_items.append({"name": store_item_name, "cost": store_item_cost, "element": store_elem_list[i]})
        except:
            continue  # Ignore errors if parsing fails for any element

    return store_items

# Function to click on the most expensive affordable store item
def buy_most_expensive_item(current_money, store_items):
    affordable_items = [item for item in store_items if item["cost"] <= current_money]
    
    if affordable_items:
        # Buy the most expensive item that is affordable
        best_item = max(affordable_items, key=lambda x: x["cost"])
        best_item["element"].click()
        print(f"Bought: {best_item['name']} for {best_item['cost']} cookies")

# Main loop: click the cookie, check money, and buy items
while True:
    # Click the cookie multiple times
    for _ in range(10):
        click_cookie.click()
    
    # Get the current money
    int_money = get_current_money()
    
    # Fetch the store items
    store_items = get_store_items()
    
    # Try to buy the most expensive affordable item
    buy_most_expensive_item(int_money, store_items)
    
    # Sleep for a short while to avoid overwhelming the site
    time.sleep(.1)

# Close the driver (unreachable in this loop, but should be here in a final version)
# driver.quit()
