import youtube_dl

link = ["https://www.youtube.com/watch?v=hXM1jzaXQOs"]

ydl = youtube_dl.YoutubeDL()
ydl.download(link)