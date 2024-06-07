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
    driver.get("https://automated.pythonanywhere.com")
    return driver


def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_driver()
    count = 10
    # wait 2 seconds for the dynamic value to populate
    time.sleep(2)

    while count > 0:
        # create the fileName
        fileName = f"{time.localtime()[0]}-{time.localtime()[1]}-{time.localtime()[2]}.{time.localtime()[3]}-{time.localtime()[4]}-{time.localtime()[5]}"
        new_file = open(f"{fileName}.txt", 'w')

        print(fileName)
        # grab the dynamic value
        element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
        new_file.write(str(clean_text(element.text)))
        time.sleep(2)
        count -= 1
        new_file.close()

    driver.quit()


main()
