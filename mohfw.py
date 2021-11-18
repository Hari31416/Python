from selenium import webdriver
import datetime

# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    executable_path=r"C:\Users\harik\AppData\Local\geckodriver-v0.30.0-win64\geckodriver.exe"
)


driver.get("https://www.mohfw.gov.in/")
driver.find_element(By.CLASS_NAME, "imgmenu").click()
date = datetime.datetime.now().strftime("%d-%m-%Y")
driver.find_element(By.CLASS_NAME, "data-table").screenshot(
    f"c:\\Users\\harik\\Desktop\\{date}mohfw.png"
)
driver.quit()