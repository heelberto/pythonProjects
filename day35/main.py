from twilio.rest import Client
import os

account_sid = os.environ.get("_TWILIO_ACCT_SID_")
auth_token = os.environ.get("_TWILIO_AUTH_TOKEN_")
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18667516986',
  body='Hello from Twilio',
  to='+17147078504'
)

print(message.status)
print(message.sid)
