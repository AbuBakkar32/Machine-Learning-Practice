import youtube_dl

# link = input("Paste your copy youtube downloadable link \n")
link = input("Paste your copy youtube downloadable link \n")

ydl = youtube_dl.YoutubeDL()
ydl.download([link])
