import os
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload
from cleanlinks import *

CLIENT_SECRET_FILE = 'client_secret.JSON'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

# Ensure you have the correct list of file IDs

# file_ids = ids
file_ids = [
    '1omC0_OuTpiZjrpulu0D78BN_yLs3bRp7',
    '1oi9SEtXxNejZBDmKHqBGfyZfAE2QdgaP',
    '16XVsZaeLg_3odyk-WcrhAvtdhBIAkKRJ',
    '1O6337giXCSB8e4SvPmKAXcOW4rTAgCp0'
]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
i = 0
for file_id in file_ids:
    # Retrieve file information including the original file name
    file_info = service.files().get(fileId=file_id).execute()
    # myinfo = service.files().fileExtension

    # Get the original file name
    original_file_name = str(i) + file_info['name']
    i = i + 1

    # Create a request to get the media content of the file using the file ID
    request = service.files().get_media(fileId=file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done = False

    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

    fh.seek(0)

    with open(os.path.join('./mygoogleapi/imgs', original_file_name), 'wb') as f:
        f.write(fh.read())

print("Downloaded all files with their original names.")
print(len(file_ids))

""" import os, io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload
from cleanlinks import *

CLIENT_SECRET_FILE = 'client_secret.JSON'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES =['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

file_ids = ids

file_names = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png', '11.png', '12.png', '13.png','14.png', '15.png', '16.png', '17.png', '18.png', '19.png', '20.png', '21.png']

for file_id, file_name in zip(file_ids, file_names):
    request = service.files().get_media(fileId=file_id)
    
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done = False

    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

        fh.seek(0)

        with open(os.path.join('./random', file_name), 'wb') as f:
            f.write(fh.read())
            f.close()
 """

""" file_names = ['test.png', 'test2.png']

for file_id, file_name in zip(file_ids, file_names):
    request = service.files().get_media(fileId=file_id)
    
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done = False

    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

        fh.seek(0)

        with open(os.path.join('./random', file_name), 'wb') as f:
            f.write(fh.read())
            f.close()

 """
