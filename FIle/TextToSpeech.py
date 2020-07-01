from gtts import gTTS
import os

file = open('text.txt', 'r')
read = file.read().replace('\n', ' ')
output = gTTS(text=read, lang='en', slow=False, lang_check=False)
output.save('output.mp3')
file.close()
os.system('start output.mp3')