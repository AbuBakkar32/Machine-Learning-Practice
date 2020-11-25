from twilio.rest import Client

acount_sid = "AC3a87a952ec577a10637156aa4c7e8b85"
token_auth = "c3c4bd6bba9f4ff08ab8e5304964f6f3"
client = Client(acount_sid, token_auth)

Message = input("Write Your Text Here: ")
Sms_sent_to = input("SMS Send To: ")

client.messages.create(from_="+17195694678",
                       body=Message,
                       to=Sms_sent_to)
print("Thank you Abu Bakkar Siddik for sending a Message")
