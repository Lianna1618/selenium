import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/login")

# Correct usage of find_element with named parameters (Selenium 4.3+)
driver.find_element(
    by="xpath", value='//*[@id="login_email"]'
    ).send_keys("test_email")
driver.find_element(
    by="xpath", value='//*[@id="password"]'
    ).send_keys("test_password")

time.sleep(5)

# ➖ ID = "id"
# ➖ XPATH = "xpath"
# ➖ NAME = "name"
# ➖ CLASS_NAME = "class name"
# ➖ CSS_SELECTOR = "css selector"
