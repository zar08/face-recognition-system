from gtts import gTTS
import os

"""def greeting_users(name):
    name"""
mytext = "Hi, this is an example of converting text to audio. This is a bot speaking here, not a real human!"
audio = gTTS(text=mytext, lang="en", slow=False)

audio.save("example.mp3")
os.system("start example.mp3")