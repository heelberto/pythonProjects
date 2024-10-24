import requests
from bs4 import BeautifulSoup
import smtplib
import os
import datetime

import pprint

# constants
EMAIL = os.environ.get("_PYTHON_EMAIL_")
PASSWORD = os.environ.get("_PYTHON_EMAIL_PASSWORD_")
TARGET_PRICE = 100.00
#Accept-Language:en-US,en;q=0.9
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
#User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"

def email_alert(current_price, target_price):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        response = requests.get("https://appbrewery.github.io/instant_pot/")
        web_page_text = response.text
        soup = BeautifulSoup(web_page_text, "html.parser")
        product_title = soup.find(name="span", id="productTitle").text
        if current_price < target_price:

            letter_contents = (f"Product: Instant Pot 's Price has dropped below ${TARGET_PRICE}!"
                                    f"That's a current savings if {target_price-current_price}")
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:***PRICE DROP ALERT***\n\n{letter_contents}")
            print("Email Alert Sent!")


def read_and_retrieve_price():
    header={
        "Accept-Language": ACCEPT_LANGUAGE,
        "User-Agent": USER_AGENT
    }
    response = requests.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1", headers=header)
    print(response.status_code)
    web_page_text = response.text
    soup = BeautifulSoup(web_page_text, "html.parser")
    whole_num = soup.find(name="span", class_="a-price-whole").text
    whole_num = whole_num.strip(".")
    dec_num = soup.find(name="span", class_="a-price-fraction").text
    return float(f"{whole_num}.{dec_num}")



def main():
    cur_price = read_and_retrieve_price()
    email_alert(cur_price, TARGET_PRICE)

if __name__ == "__main__":
    main()
