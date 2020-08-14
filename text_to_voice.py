from gtts import gTTS #pip3 install gTTS using COmmand Prompt
import os
text=input("Enter your text: ")
language='en'
conv=gTTS(text=text,lang=language,slow=False)
conv.save("audio.mp3")
os.system("audio.mp3")
