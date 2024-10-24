from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta

def main():

    #create connection to the website
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://orteil.dashnet.org/experiments/cookie/")

    # find cookie element
    cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")



    # create an original timestamp
    now = datetime.now()

    # create the 5 minute timestamp
    now_5 = datetime.now()

    while True:
        cookie.click()
        cur_time = datetime.now()

        if cur_time - now_5 > timedelta(minutes=5):
            break

        if cur_time - now > timedelta(seconds=5):

            # find and make a list of different powerups
            cursor = driver.find_element(By.CSS_SELECTOR, value="#buyCursor")
            grandma = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma")
            factory = driver.find_element(By.CSS_SELECTOR, value="#buyFactory")
            mine = driver.find_element(By.CSS_SELECTOR, value="#buyMine")
            shipment = driver.find_element(By.CSS_SELECTOR, value="#buyShipment")
            alchemy = driver.find_element(By.ID, value="buyAlchemy lab")
            portal = driver.find_element(By.CSS_SELECTOR, value="#buyPortal")
            time_machine = driver.find_element(By.ID, value="buyTime machine")
            shopping_options = [cursor, grandma, factory, mine, shipment, alchemy, portal, time_machine]

            now = datetime.now()
            most_expensive_index_value = -1
            index_to_buy = 0
            try:
                cur_balance = int(driver.find_element(By.ID, value="money").text)
            except ValueError:
                cur_balance = int(driver.find_element(By.ID, value="money").text.replace(",",""))
            for index in range(len(shopping_options)):
                try:
                    index_cost = int(shopping_options[index].text.split("\n")[0].split(" ")[-1])
                except ValueError:
                    index_cost = int(shopping_options[index].text.split("\n")[0].split(" ")[-1].replace(",", ""))
                # print(index_cost)
                if index_cost > most_expensive_index_value and cur_balance > index_cost:
                    most_expensive_index_value = index_cost
                    index_to_buy = index
                #print(index_cost)
            shopping_options[index_to_buy].click()

if __name__ == "__main__":
    main()
