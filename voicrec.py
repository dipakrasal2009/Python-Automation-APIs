import pyaudio
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# List available audio input devices
audio = pyaudio.PyAudio()
for i in range(audio.get_device_count()):
    device_info = audio.get_device_info_by_index(i)
    print(f"Device {i}: {device_info['name']}")

# Function to capture audio and recognize speech
def recognize_speech(device_index):
    with sr.Microphone(device_index=device_index) as source:
        print("Say something...")
        audio = recognizer.listen(source)
        
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")

        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# Replace `device_index` with the appropriate index number from the listed devices
recognize_speech(device_index=3)

