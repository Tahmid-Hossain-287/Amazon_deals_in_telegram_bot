import os, time
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import traceback


options = Options()
# Specifying where the cookies will be stored.
options.add_argument("--user-data-dir=C:\\Users\\Tahmid\\Programming\\automation\\cookies")
# Silences logs on terminal and keeps terminal looking clean.
# os.environ['WDM_LOG_LEVEL'] = '0'
# Saves driver on project directory.
os.environ['WDM_LOCAL'] = '1'
# Downloads and installs necessary driver version if already not done so.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
actions = action_chains.ActionChains(driver)

# Setting window position and size.
driver.set_window_size(1260, 905) # Resizes the window to a specific size.
driver.set_window_position(250, 70, windowHandle='current')

print('Driver instantiated successfully')
