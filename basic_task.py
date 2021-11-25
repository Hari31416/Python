from selenium import webdriver
import datetime
import time


# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    executable_path=r"C:\Users\harik\AppData\Local\geckodriver-v0.30.0-win64\geckodriver.exe"
)
driver.get("https://www.mohfw.gov.in/")

time.sleep(5)
driver.close()
