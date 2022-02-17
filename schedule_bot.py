import os, random
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
from product_link_scrape import launch_deals_page, all_deals, retrieve_affiliate_link, go_next_page, multiple_deals_to_one_deal
from telegram_bot import launch_page, get_product_information, send_telegram_message
from secrets import link, pages_to_retrieve, start_time, time_to_collect_deals
import schedule


def run_amazon_bot():
    launch_deals_page(url=link)
    all_deals(pages_to_retrieve_upto=pages_to_retrieve)

def run_telegram_bot():
    launch_page()
    send_telegram_message()

def hello_world():
    while True:
        print("Hello World")
        sleep(2)

schedule.every().day.at(time_to_collect_deals).do(run_amazon_bot)
schedule.every().day.at(start_time).do(run_telegram_bot)

while True:
    schedule.run_pending()
    sleep(1)


