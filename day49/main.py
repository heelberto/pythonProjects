import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pprint

# constants
WEBSITE = "https://www.linkedin.com/jobs/search/?currentJobId=3980105243&f_AL=true&keywords=software%20engineer%20intern&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
_LINKEDIN_UN_ = os.environ.get("_LINKEDIN_EMAIL_")
_LINKEDIN_PW_ = os.environ.get("_LINKEDIN_PW_")

def main():
    # create connection to the website
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f"{WEBSITE}")

    # find sign in button
    sign_in_button = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
    sign_in_button.click()
    time.sleep(2)

    # find email/pw input
    email_input = driver.find_element(By.NAME, value="session_key")
    email_input.send_keys(f"{_LINKEDIN_UN_}")
    password_input = driver.find_element(By.NAME, value="session_password")
    password_input.send_keys(f"{_LINKEDIN_PW_}")
    sign_in_submit = driver.find_element(By.XPATH, value="/html/body/div/main/div[2]/div[1]/form/div[3]/button")
    sign_in_submit.click()
    time.sleep(2)

    easy_apply_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
    easy_apply_button.click()

    time.sleep(2)
    next_button = driver.find_element(By.CSS_SELECTOR, value="button .artdeco-button")
    next_button.click()

    time.sleep(1)
    sec_next_button = driver.find_element(By.CSS_SELECTOR, value="button .artdeco-button")
    sec_next_button.click()





if __name__ == "__main__":
    main()
