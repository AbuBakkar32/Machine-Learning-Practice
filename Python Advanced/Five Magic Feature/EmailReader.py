import imaplib
import email

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('rakibsarkar26@gmail.com', 'gjutblvmtfnlydsk')
mail.list()
mail.select('inbox')

(retcode, messages) = mail.search(None, '(UNSEEN)')
print(messages)
if retcode == 'OK':
    id_list = messages[0].split()
    latest_emails = id_list[:10]
    for num in latest_emails:
        typ, data = mail.fetch(num, '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                original = email.message_from_bytes(response_part[1])
                mail.store(num, '+FLAGS', '\\Seen')
                print(original['From'])

mail.close()
mail.logout()

