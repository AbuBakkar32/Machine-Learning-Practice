import youtube_dl

links = []
link = input("Paste your copy youtube downloadable link \n")
links.append(link)

ydl = youtube_dl.YoutubeDL()
ydl.download(links)
print("♦♦♦Thank for using this apps♦♦♦")
