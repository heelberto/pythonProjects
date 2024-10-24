##################### Extra Hard Starting Project ######################
import pandas
import random
import smtplib
import datetime

my_email = "pythontest281330@gmail.com"
password = "pvlh owgr dlfr blho"

# convert csv to dict
birthdays_df = pandas.read_csv("birthdays.csv")
birthdays_dict = birthdays_df.to_dict(orient="records")

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    now = datetime.datetime.now()
    for person in birthdays_dict:
        if now.month == person["month"] and now.day == person["day"]:
            with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as letter:
                letter_contents = letter.read()
                letter_contents = letter_contents.replace("[NAME]", f"{person['name']}")
                print(letter_contents)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=f"{person['email']}",
                                    msg=f"Subject:Happy Birthday\n\n{letter_contents}")

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




