import os, requests
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from bs4 import BeautifulSoup


options = Options()
# Specifying where the cookies will be stored.
options.add_argument("--user-data-dir=C:\\Users\\Tahmid\\Programming\\telegram_bot\\cookies")
# Silences logs on terminal and keeps terminal looking clean.
os.environ['WDM_LOG_LEVEL'] = '0'
# Saves driver on project directory.
os.environ['WDM_LOCAL'] = '1'
# Downloads and installs necessary driver version if already not done so.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
actions = action_chains.ActionChains(driver)

# Setting window position and size.
driver.set_window_size(1260, 905) # Resizes the window to a specific size.
driver.set_window_position(250, 70, windowHandle='current')

print('Driver instantiated successfully')

# Launches the today's deal page.
def launch_deals_page():
    # driver.get("https://www.amazon.it/")
    driver.get("https://www.amazon.com/")

    deals_page = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#nav-xshop > a:nth-child(2)')
        )
    )

    print("deals page found")

    deals_page.click()


def page_info():
    # Retrive all the product information from the deals page.
    pass

# Goes to the next page in today's deal page.
def go_next_page(page_number_to_go):
    for page_number in range(page_number_to_go-1):
        next_button = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable(
                # (By.XPATH, '//*[@id="nav-xshop"]/a[1]')
                (By.CLASS_NAME, 'a-last')
            )
        )

        sleep(1.5)
        next_button.click()
    print('went to the next page')




def main():
    launch_deals_page()

if __name__ == "__main__":
    main()