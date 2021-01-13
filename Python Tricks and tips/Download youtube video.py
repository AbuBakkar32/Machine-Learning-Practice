import youtube_dl

link = input("Paste your copy youtube downloadable link")

ydl = youtube_dl.YoutubeDL()
ydl.download(link)
print("♦♦♦Thank for using this App♦♦♦")
