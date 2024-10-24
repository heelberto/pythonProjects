import os
import requests
from twilio.rest import Client

TWILIO_SID = os.environ.get("_TWILIO_SID_")
TWILIO_TOKEN = os.environ.get("_TWILIO_TOKEN_")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.sid = TWILIO_SID
        self.token = TWILIO_TOKEN
        self.client = Client(self.sid, self.token)

    def send_notification(self, prev_low, new_low):
        _body = f"Found a cheaper flight!\n" + f"Previous cheapest flight : ${prev_low}\nNew cheapest flight : ${new_low}" + f"That's a savings of ${float(prev_low) - float(new_low)}"
        message = self.client.messages.create(
            from_='+18444640179',
            body=_body,
            to='+17147078504'
        )
