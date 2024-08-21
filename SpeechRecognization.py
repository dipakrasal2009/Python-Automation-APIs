import speech_recognition as sr
import webbrowser
# Initialize recognizer
recognizer = sr.Recognizer()

# Capture voice input from the microphone
with sr.Microphone() as source:
    print("how can I help you :=>  ")
    # Adjust the recognizer sensitivity to ambient noise
    recognizer.adjust_for_ambient_noise(source, duration=1)
    # Capture the audio from the microphone
    audio = recognizer.listen(source)

# Recognize speech using Google Web Speech API
try:
    string = recognizer.recognize_google(audio)
    print("You Speak =>  " + string)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")

if 'Firefox' in string:
    #import webbrowser

    # Open Firefox
    firefox_path = '/usr/bin/firefox'  # Specify the path to the Firefox executable if necessary

    # Register Firefox browser
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

    # Open a URL in Firefox
    webbrowser.get('firefox').open('http://www.google.com')

