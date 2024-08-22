from gtts import gTTS
import os

def text_to_audio(text, filename='output.mp3'):
    tts = gTTS(text)
    tts.save(filename)
    os.system(f'mpg321 {filename}')
