import smtplib
import string
import random
from email.message import EmailMessage


def randPass():
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    size = 5
    return ''.join(random.choice(chars) for _ in range(size, 12))


# customer = ['sowrov35-1946@diu.edu.bd', 'sabbir35-2007@diu.edu.bd', 'sowrov35-1946@diu.edu.bd',
#             'tuhin35-1947@diu.edu.bd', 'afrail35-2016@diu.edu.bd', 'najmul35-1775@diu.edu.bd', 'sabbir35-1979@diu.edu.bd']

try:
    email = 'abubakkar.swe@gmail.com'
    password = 'Abubakkar32'
    send_to_email = 'Rakibsarkar26@gmail.com'

    msg = EmailMessage()
    msg['Subject'] = 'Facebook'
    msg['From'] = email
    msg['To'] = send_to_email

    TEXT = f'Hello,\nYour Email Verification Code Is :{randPass()}'
    msg.set_content(TEXT)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.send_message(msg)
    print('Successfully Mail has been Send!!!!')
    server.quit()
except:
    print("Opps!! Try Again Please")
