import webdriver_manager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from IPython.display import clear_output
import pandas as pd
import time


class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.browser = "Chrome"
        # self.driver = webdriver.Firefox(
        #     executable_path=r"C:\Users\harik\AppData\Local\geckodriver-v0.30.0-win64\geckodriver.exe"
        # )
        # self.driver.maximize_window()


class Webpage:
    def __init__(self, url):
        self.url = url
        the_driver = Driver()
        self.driver = the_driver.driver

    def open(self):
        self.driver.get(self.url)


class Account(Webpage):
    def __init__(self, email):
        self.email = email
        self.password = email[:8]

    def register(self):
        """
        Registers a new user on https://singlelogin.org/registration.php
        returns the email address of the user
        """
        ### emails to add in database
        login_details = pd.read_csv("login_details.csv")
        emails = list(login_details["email"])
        passwords = list(login_details["password"])

        # Step 1
        print("Going to registartion page")
        regster = Webpage("https://singlelogin.org/registration.php")
        regster.open()
        print("Done!")

        # Step 2
        print("Filling in the form")
        # Email
        email_entry = self.driver.find_element(By.NAME, "email")
        email_entry.clear()
        email_entry.send_keys(self.email)

        # Password
        password_entry = self.driver.find_element(By.NAME, "password")
        password_entry.clear()
        password_entry.send_keys(self.password)
        print("Done!")
        # Step 3
        print("Submitting the form")
        # Submit Button
        submit_button = self.driver.find_element(By.TAG_NAME, "form button")
        submit_button.click()
        print("Done!")
        print("Adding these to the csv file")
        try:
            emails.append(self.email)
            passwords.append(self.password)
            df = pd.DataFrame(data=[emails, passwords]).T
            df.columns = ["email", "password"]
            df.to_csv("login_details.csv", index=False)
        except:
            print("You should add this email to database")
            return self.email
        return self.email

    def login(self):
        """
        Logs in to https://singlelogin.org/
        """

        # Step 1
        print("Going to login page")
        self.driver.get("https://singlelogin.org")
        print("Done!")

        print("Filling in the form")
        # Step 2
        # Email
        email_entry = self.driver.find_element(By.NAME, "email")
        email_entry.clear()
        email_entry.send_keys(self.email)

        # Password
        password_entry = self.driver.find_element(By.NAME, "password")
        password_entry.clear()
        password_entry.send_keys(self.password)
        print("Done!")

        print("Submitting the form")
        # Step 3
        # Submit Button
        submit_button = self.driver.find_element(By.TAG_NAME, "form button")
        submit_button.click()
        print("Done!")
        time.sleep(5)
        return True


# acc = Account("penol29169@gyn5.com")

# acc.login()
# driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
