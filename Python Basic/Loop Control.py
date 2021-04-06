import time
password = 'abu'
pw = ''
auth = False
count = 0
max_attempt = 3
start = time.time()

while pw != password:
    count = count+1
    if count > max_attempt:
        break
    pw = input(f'{count}: What is the password? ')
else:
    auth = True

output = 'Authoried' if auth else 'Account Locked' # ternary operation
print(output)
print(time.time()-start)