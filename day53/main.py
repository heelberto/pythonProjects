import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import pprint

# constants
FORM_ADDRESS = "https://docs.google.com/forms/d/e/1FAIpQLSel3pioMaVnjavGzk5afrcxRZrL7s8CaiEVNGX6tQUA0TwAfw/viewform?usp=sf_link"
ZILLOW_ADDRESS = "https://appbrewery.github.io/Zillow-Clone/"


def main():
    # create connection to form
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(name="detach", value=True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url=FORM_ADDRESS)

    # create connection to zillow site
    zillow_site = requests.get(ZILLOW_ADDRESS)
    soup = BeautifulSoup(zillow_site.text, "html.parser")

    listings_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
    addresses = soup.find_all(name="address")
    links = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
    listing_values = []
    address_list = []
    links_list = []
    print(len(links))

    for i in range(len(listings_prices)):
        listing_values.append(int(listings_prices[i].text[:6].replace("$", "").replace(",", "").replace("+", "")))
        address_list.append(addresses[i].text.strip())
        links_list.append(links[i]['href'])

    for i in range(44):
        address_input = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        address_input.send_keys(address_list[i])
        time.sleep(3)
        price_input = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        price_input.send_keys(str(listing_values[i]))
        time.sleep(3)
        link_input = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        link_input.send_keys(links_list[i])
        time.sleep(3)
        submit_button = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")
        submit_button.click()
        next_form_button = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
        next_form_button.click()




if __name__ == "__main__":
    main()
