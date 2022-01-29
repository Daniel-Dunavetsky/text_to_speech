from gtts import gTTS
import os

vtext = ("test")

languge = ("en")


myobj = gTTS(text=vtext, lang = languge, slow = False)


myobj.save("test.mp3")

os.system("test.mp3")