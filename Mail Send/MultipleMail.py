import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

email = 'myaddress@gmail.com'
password = 'password'
send_to_emails = ['sentoaddreess@gmail.com', 'sentoaddreess2@gmail.com'] # List of email addresses
subject = 'This is the subject'
message = 'This is my message'
file_location = 'C:\\Users\\You\\Desktop\\attach.txt'

# Create the attachment file (only do it once)
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# Connect and login to the email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)

# Loop over each email to send to
for send_to_email in send_to_emails:
    # Setup MIMEMultipart for each email address (if we don't do this, the emails will concat on each email sent)
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))
    # Attach the attachment file
    msg.attach(part)

    # Send the email to this specific email address
    server.sendmail(email, send_to_email, msg.as_string())

# Quit the email server when everything is done
server.quit()