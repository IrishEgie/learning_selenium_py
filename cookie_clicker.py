import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import StaleElementReferenceException
import time

# Configure options for the browser
options = Options()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0")

driver = webdriver.Firefox(options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Fetch the web elements for cookie clicking and store items
click_cookie = driver.find_element(By.CSS_SELECTOR, value='div #cookie')

# Dictionary to track the original costs of items
original_item_costs = {}

# Function to fetch current money and convert to an integer
def get_current_money():
    money = driver.find_element(By.CSS_SELECTOR, value="div #money").text.replace(",", "")
    if money.isdigit():
        return int(money)
    return 0

# Function to extract the numerical cost from a string using regex
def extract_cost(text):
    cost = re.findall(r'\d+', text)
    return int(cost[0].replace(",", "")) if cost else None

# Function to fetch available store items and their costs
def get_store_items():
    store_elem_list = driver.find_elements(By.CSS_SELECTOR, value="div #rightPanel #store div")
    store_elem_cost_list = driver.find_elements(By.CSS_SELECTOR, value="div #rightPanel #store div b")
    store_items = []
    
    for i in range(len(store_elem_cost_list) - 1):
        try:
            store_item_text = store_elem_list[i].text
            store_item_split = store_item_text.split(" - ")

            if len(store_item_split) == 2:
                store_item_name = store_item_split[0]
                store_item_cost = extract_cost(store_item_split[1])
                
                # Ensure the cost is valid
                if store_item_cost is not None:
                    if store_item_name not in original_item_costs:
                        original_item_costs[store_item_name] = store_item_cost

                    store_items.append({
                        "name": store_item_name,
                        "cost": store_item_cost,
                        "element": store_elem_list[i]
                    })
            else:
                print(f"Skipping item: {store_item_text}")  # Debugging information to spot problematic items
        except Exception as e:
            print(f"Error parsing item: {e}")
            continue  # Ignore errors if parsing fails for any element
 # Debugging: print first two items
    return store_items

# Function to click on the most expensive affordable store item
def buy_most_expensive_item(current_money, store_items):
    affordable_items = []
    
    for item in store_items:
        original_cost = original_item_costs.get(item["name"], item["cost"])
        # Only consider the item if its current cost is not more than 50% above the original
        if item["cost"] <= current_money and item["cost"] <= original_cost * 1.75:
            affordable_items.append(item)
    
    if affordable_items:
        # Buy the most expensive affordable item
        best_item = max(affordable_items, key=lambda x: x["cost"])
        try:
            best_item["element"].click()
            # Fetch the text of the clicked item directly from the element
            clicked_item_text = best_item["element"].text
            print(f"Bought: {clicked_item_text}")
        except StaleElementReferenceException:
            print(f"Could not click on: {best_item['name']}, element is stale.")


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
    time.sleep(0.5)

# Close the driver (unreachable in this loop, but should be here in a final version)
# driver.quit()
