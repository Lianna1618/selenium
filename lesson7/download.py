import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

download_dir = os.path.join(os.getcwd(), "img_files")


chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_dir}

chrome_options.add_experimental_option("prefs", prefs)
chrome_options.page_load_strategy = "normal"
chrome_options.add_argument("--window-size=1440,900")
chrome_options.add_argument("--disable-extensions")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://the-internet.herokuapp.com/download")

time.sleep(2)

driver.find_element("xpath", "//a[text()='webdriverIO.png']").click()

time.sleep(5)
