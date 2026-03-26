import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_driver():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    driver_path = os.path.join(base_dir, "drivers", "chromedriver.exe")

    service = Service(driver_path)

    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)

    return driver