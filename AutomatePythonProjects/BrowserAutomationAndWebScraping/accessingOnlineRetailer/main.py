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
    driver.get("https://www.twitch.tv/")
    return driver

def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()

    """
    # login with my account info
    driver.find_element(By.ID, "CustomerEmail").send_keys("xxgilbert1997@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "CustomerPassword").send_keys("password1")

    # click on the contact us link
    driver.find_element(By.XPATH, "/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()

    # enter an order number
    driver.find_element(By.XPATH, "/html/body/main/article/div/section/div/form/div[4]/input").send_keys("1234567890")

    # enter a phone number
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/main/article/div/section/div/form/div[5]/input").send_keys("2813308004")

    # enter a message
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/main/article/div/section/div/form/div[7]/textarea").send_keys("Who?! MIKE JONES!!")
    time.sleep(3)

    driver.find_element(By.XPATH, "/html/body/main/article/div/section/div/form/input[3]").click()

    print(driver.current_url)
    """

    # twitch experiment

    # click the login
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button/div/div").click()
    time.sleep(1)
    #log in with my info
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[1]/div/div[2]/div/input").send_keys("heelberto")
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[2]/div/div[1]/div[2]/div[1]/div/input").send_keys("DoubleDoubleAnimalStyle789*")
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/button/div/div").click()
    time.sleep(5)
    #go to the streaming channel
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/nav/div/div[1]/div[2]/div[3]/div[1]/div/div/a/div[2]/div/div[1]/div[1]/p").click()
    time.sleep(5)

    count = 10

    while count > 0:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div[1]/aside/div/div/div[2]/div/div/section/div/div[6]/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]").send_keys(f"{str(count)}" + Keys.RETURN)
        time.sleep(1)
        count -= 1

    #click on the chat and send text
    print(driver.current_url)


    driver.quit()


main()
