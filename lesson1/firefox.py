from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Set up the Firefox driver with WebDriver Manager
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)


# Firefox
