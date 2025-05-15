import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

url = driver.current_url
print("Current URL:", url)
assert url == "https://www.wikipedia.org/", "Error in URL"

title = driver.title
print("Page Title:", title)
assert title == "Wikipedia", "Error in Title"

print(driver.page_source)


time.sleep(5)
