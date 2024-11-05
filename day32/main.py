import smtplib
import datetime
import random

my_email = "pythontest281330@gmail.com"
my_yahoo_email = "pythontest281330@yahoo.com"
password = "pvlh owgr dlfr blho"
quote_list = []

with open("quotes.txt", "r") as file:
    for line in file:
        quote_list.append(line)
    print(quote_list)


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    now = datetime.datetime.now()
    if now.weekday() == 0:
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Hello\n\n{random.choice(quote_list)}")

