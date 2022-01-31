from pdb import line_prefix
import telegram
from secrets import token, group_1_id
from time import sleep
import os, requests, random
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from time import sleep
import re

# Note that your bot will not be able to send more than 20 messages per minute to the same group.
bot = telegram.Bot(token=str(token))
updates = bot.get_updates()
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

# template = " 🔥🔥 23% OFF 🔥🔥 \n 🤑 SUPER SCONTO 🤑  \n 👉 Apri su Amazon amzn.to/347C4FE"
def get_discount(link):
    try:
        driver.get(link)
        discount_amount = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (By.CLASS_NAME, 'a-span12.a-color-price.a-size-base')
                        )
                    )
        raw_discount = str(discount_amount.text)
        discount_amount = (re.search('\((.*?)\)', raw_discount)).group(1)
        # print(discount_amount)
        return discount_amount
        # with open('discount.txt', 'a') as file:
        #     file.write(discount_amount + "\n")
    except:
        pass


with open('deals.txt') as file:
    lines = file.readlines()
    for line in lines:
        discount = get_discount(line)
        template = f" 🔥🔥 {discount} 🔥🔥 \n 🤑 SUPER SCONTO 🤑  \n 👉 Apri su Amazon {line}"
        bot.send_message(text= template, chat_id=group_1_id)
        sleep(3)