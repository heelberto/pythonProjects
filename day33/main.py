from tkinter import *
import requests
import datetime

"""
def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()

    if response.status_code != 404:
        request_dict = response.json()
        canvas.itemconfig(quote_text, text=f"{request_dict['quote']}")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
"""
parameters = {
    "lat": 33.7175,
    "lng": 117.8311,
    "formatted": 0,
    "tzid": "PT"
}

now = datetime.datetime.now()

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

split_sunrise = sunrise.split("T")

print(sunrise)
print(sunset)

