import os, requests
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
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


def all_deals():
    # retrieve all the product information from the deals page.
    deals = WebDriverWait(driver, 4).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, 'DealGridItem-module__dealItemContent_1vFddcq1F8pUxM8dd9FW32')
        )
    ) # All the items listed for sale.
    for item in range(len(deals)):
        deals_second_time = WebDriverWait(driver, 4).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, 'DealGridItem-module__dealItemContent_1vFddcq1F8pUxM8dd9FW32')
        )
    )
        deals_second_time[item].click()
        retrieve_affiliate_link()
        sleep(2)
        driver.back()
        sleep(1)
    # for item in deals:
        # item.send_keys(Keys.CONTROL + 't')
        # break
    #     item.click()
    #     retrieve_affiliate_link()
    #     sleep(2)
    #     driver.back()
    #     sleep(1)

def retrieve_affiliate_link():
    # Copies the affiliate short link and saves on deals.txt file.
    produce_short_link = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#amzn-ss-text-link > span > strong > a')
        )
    )
    produce_short_link.click()
    
    short_link = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located(
            (By.ID, 'amzn-ss-text-shortlink-textarea')
        )
    )

    with open('deals.txt', 'a') as notebook:
        notebook.write(short_link.text + "\n")
    
    
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
    all_deals()

if __name__ == "__main__":
    main()

