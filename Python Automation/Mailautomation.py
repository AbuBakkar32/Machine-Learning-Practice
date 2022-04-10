import yagmail

receiver = "abu35-1994@diu.edu.bd"
message = ("Hello there! this is most important mail")

sender = yagmail.SMTP("sender email")
sender.send(to=receiver, subject="Yagmail test with attachment", contents=message)
