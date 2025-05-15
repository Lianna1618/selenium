import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/global")

time.sleep(5)

log_btn = driver.find_element(by="xpath", value='//*[@id="login-desktop"]')
log_btn.click()
time.sleep(5)

email_input = driver.find_element(by="xpath", value='//*[@id="login_email"]')
email_input.send_keys("test_email")
print(email_input.get_attribute("value"))
time.sleep(5)

pass_input = driver.find_element(by="xpath", value='//*[@id="password"]')
pass_input.send_keys("test_password")
print(pass_input.get_attribute("value"))
time.sleep(5)

email_input.clear()

email_input.send_keys("test@gmail.com")
print(email_input.get_attribute("value"))
time.sleep(5)