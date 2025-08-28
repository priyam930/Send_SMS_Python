from twilio.rest import Client

# Your Twilio credentials
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello! This is a test SMS sent using Python ✅",
    from_="+1 304 721 1950",   # Your Twilio phone number
    to="+919301423057"     # Receiver's phone number (with country code)
)

print("Message sent! SID:", message.sid)
