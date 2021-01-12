# a simple script to block websites
from datetime import datetime

end_time = datetime(2021, 1, 4, 20)  # y, m, d, h, min

sites_to_block = ['www.facebook.com', 'facebook.com']

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"


def block_websites():
    if datetime.now() < end_time:
        print("Block sites")
        with open(hosts_path, 'r+') as hostfile:
            hosts_content = hostfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostfile.write(redirect + ' ' + site + '\n')
    else:
        print('Unblock sites')
        with open(hosts_path, 'r+') as hostfile:
            lines = hostfile.readlines()
            hostfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostfile.write(line)
            hostfile.truncate()


# sudo python main.py
if __name__ == '__main__':
    block_websites()
