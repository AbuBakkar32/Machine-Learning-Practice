import re

data = '''loltukku loltukku_pandi@gmail.com vandu vandumurgan@hotmail.com
kattu katuupuchi@gmail.com pandi powerpandi@gmail.com powerpandi@hotmail.com'''
list_user = data.split()
gmail_user = ['Gmail User:', ]
hotmail_user = ['Hotmail User:']

for email in list_user:
    if re.search(r'\w+@gmail.\w+', email):
        gmail_user.append(email)
    elif re.search(r'\w+@hotmail.\w+', email):
        hotmail_user.append(email)

gmail_user.append('')
for i in gmail_user, hotmail_user:
    for j in i:
        print(j)
