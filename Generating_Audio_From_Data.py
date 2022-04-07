from gtts import gTTS
import os
text="Today is a good day"
output=gTTS(text=text,lang='en',slow=False)
output.save('output.mp3')
os.system('start output.mp3')