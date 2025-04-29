import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
 print("Please speak something:")
 audio = recognizer.listen(source,timeout=5)

 try:
  text = recognizer.recognize_google(audio)
  print(f"You said: {text}")
 except:
  print("Sorry, I could not understand.")
