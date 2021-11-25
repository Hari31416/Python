import webdriver_manager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from IPython.display import clear_output
import pandas as pd
import time

driver = webdriver.Chrome(ChromeDriverManager().install())


def register(email):
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
    driver.get("https://singlelogin.org/registration.php")
    print("Done!")

    # Step 2
    print("Filling in the form")
    # Email
    email_entry = driver.find_element(By.NAME, "email")
    email_entry.clear()
    email_entry.send_keys(email)

    # Password
    password = email[:8]
    password_entry = driver.find_element(By.NAME, "password")
    password_entry.clear()
    password_entry.send_keys(password)
    print("Done!")
    # Step 3
    print("Submitting the form")
    # Submit Button
    submit_button = driver.find_element(By.TAG_NAME, "form button")
    submit_button.click()
    print("Done!")
    print("Adding these to the csv file")
    try:
        emails.append(email)
        passwords.append(password)
        df = pd.DataFrame(data=[emails, passwords]).T
        df.columns = ["email", "password"]
        df.to_csv("login_details.csv", index=False)
    except:
        print("You should add this email to database")
        return email
    return email


def login(email):
    """
    Logs in to https://singlelogin.org/
    """

    # Step 1
    print("Going to login page")
    driver.get("https://singlelogin.org")
    print("Done!")

    print("Filling in the form")
    # Step 2
    # Email
    email_entry = driver.find_element(By.NAME, "email")
    email_entry.clear()
    email_entry.send_keys(email)

    # Password
    password = email[:8]
    password_entry = driver.find_element(By.NAME, "password")
    password_entry.clear()
    password_entry.send_keys(password)
    print("Done!")

    print("Submitting the form")
    # Step 3
    # Submit Button
    submit_button = driver.find_element(By.TAG_NAME, "form button")
    submit_button.click()
    print("Done!")
    time.sleep(5)
    return True
