from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service('C:\\Users\\Gilbert\\Downloads\\chromedriver.exe')

def get_driver():
    # Set the following options to make browsing easier
    options = webdriver.ChromeOptions()
    # first we disable the infobars which will interfere with the script
    options.add_argument("disable-infobars")
    # begin with the browser at it's largest
    options.add_argument("start-maximized")
    # adds some compatability with linux
    options.add_argument("disable-dev-shm-usage")
    # gives greater privleges to our script
    options.add_argument("no-sandbox")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver


def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_driver()
    # find and fill in UN and PW
    driver.find_element(By.ID, "id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(By.ID, "id_password").send_keys("automatedautomated" + Keys.RETURN)

    # after signed in wait 2 seconds and click home button
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()

    # wait 2 seconds for dynamic value to load to pull
    time.sleep(2)
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
    print(clean_text(element.text))
    print(driver.current_url)


    driver.quit()


main()
