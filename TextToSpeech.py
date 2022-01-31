from gtts import gTTS
import os
from playsound import playsound
my_text = "Karunya is a Nationally Ranked, Fully Residential, Private Christian University and best university in India and its located in Coimbatore."
language = 'en'
my_obj = gTTS(text = my_text, lang = language, slow=False)
my_obj.save("Karunya.mp3")
print("Karunya.mp3 is playing")
playsound('Karunya.mp3')
