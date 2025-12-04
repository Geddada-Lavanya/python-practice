import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Suppress Chrome logs
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open Books to Scrape site
driver.get("https://books.toscrape.com/")

# Find book titles and prices
titles = driver.find_elements(By.TAG_NAME, "h3")
prices = driver.find_elements(By.CLASS_NAME, "price_color")

# Print them together
for t, p in zip(titles, prices):
    print(f"{t.text} - {p.text}")

time.sleep(5)
driver.close()
