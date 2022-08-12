from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

from selenium import webdriver

driver = webdriver.Firefox(
    executable_path=r"C:\Users\harik\AppData\Local\geckodriver-v0.30.0-win64\geckodriver.exe"
)

driver.get("https://www.mohfw.gov.in/")
driver.find_element(By.CLASS_NAME, "imgmenu").click()
driver.find_element(By.CLASS_NAME, "data-table").screenshot(
    r"c:\\Users\\harik\\Desktop\\mohfw.png"
)
