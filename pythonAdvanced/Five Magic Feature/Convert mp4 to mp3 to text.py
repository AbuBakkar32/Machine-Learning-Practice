import speech_recognition as sr
from pydub import AudioSegment

AudioSegment.from_file("/path_to_video").export("~/output.mp3", format="mp3")
sound = AudioSegment.from_mp3('output.mp3')
sound.export('transcipt.wav', format='wav')
AUDIO_FILE = 'transcipt.wav'
r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

print(r.recognize_google(audio))
