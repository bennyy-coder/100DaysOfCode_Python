from twilio.rest import Client

TWILIO_SID = "AC427b23c62214fba78b21c882ef8e"
TWILIO_AUTH_TOKEN = "0ed29ccd93ef6237b9b5b15d0e2"
TWILIO_VIRTUAL_NUMBER = "1407827"
TWILIO_VERIFIED_NUMBER = "8869122"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)