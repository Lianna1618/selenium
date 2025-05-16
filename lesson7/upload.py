import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal"
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1440,900")


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://the-internet.herokuapp.com/upload")

time.sleep(5)

driver.find_element(
    "xpath", "//*[@id='file-upload']").send_keys(f"{os.getcwd()}/img_files/webdriverIO.png"
)

time.sleep(5)
 
# "//input[type='file']"
