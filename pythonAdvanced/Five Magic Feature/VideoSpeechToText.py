import moviepy.editor as mp
import speech_recognition as sr

clip = mp.VideoFileClip(r"video_recording.mov")
clip.audio.write_audiofile(r"converted.wav")

r = sr.Recognizer()
audio = sr.AudioFile("converted.wav")

with audio as source:
    audio_file = r.record(source)
result = r.recognize_google(audio_file)

# exporting the result
with open('recognized.txt', mode='w') as file:
    file.write("Recognized Speech:")
    file.write("\n")
    file.write(result)
    print("ready!")
