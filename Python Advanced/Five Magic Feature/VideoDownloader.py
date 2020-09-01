import youtube_dl

links = ['https://www.youtube.com/watch?v=CdyWoSa44sA']

ydl_opts = {
    'format': 'bestvideo+bestaudio',
    'outtmpl': "C:/Users/abuba/Desktop" + '/%(title)s.%(ext)s'
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(links)
