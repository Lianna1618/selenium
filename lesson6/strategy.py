import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal"  # Set page load strategy
# chrome_options.add_argument("--headless")  # Run in headless mode
# chrome_options.add_argument("--disable-cache")  # Disable GPU acceleration
chrome_options.add_argument("--window-size=1440,900")  # Set window size
chrome_options.add_argument("--incognito") 
chrome_options.add_argument(
    "--ignore-certificate-errors"
)  # https://expired.badssl.com/


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

start_time = time.time()
driver.get("https://expired.badssl.com/")

end_time = time.time()
result = end_time - start_time
print(f"Page load time: {result:.2f} seconds")


# lesson6 (https://www.youtube.com/watch?v=WePIFDafLlI&list=PLN2EyQPKD10s0iwF077X5QarjEzR40M9A&index=10)