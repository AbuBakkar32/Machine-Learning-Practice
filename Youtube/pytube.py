import pytube

url = input("Enter a YouTube Video Link: ")
path = 'E:'
pytube.YouTube(url).streams.get_highest_resolution.download(path)