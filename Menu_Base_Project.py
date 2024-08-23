import yagmail
import os
import requests
from bs4 import BeautifulSoup
import geocoder
from gtts import gTTS
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import cv2
from PIL import Image, ImageDraw, ImageFilter

# Function to send an email
def send_email():
    sender_email = 'dipakrasal2009@gmail.com'
    sender_password = 'ufnmhoiswqesajsb'
    recipient_email = input("Enter the email ID you want to send the mail to: ")
    subject = input("Enter the subject of the email: ")
    content = input("Enter the body content of the email: ")

    yag = yagmail.SMTP(sender_email, sender_password)
    yag.send(
        to=recipient_email,
        subject=subject,
        contents=content
    )
    print('Email sent successfully!')

# Function to send SMS using a mobile connected via ADB
def send_sms_from_mobile():
    number = input("Enter the mobile number to send the SMS to: ")
    message = input("Enter the message: ")
    os.system(f'adb shell am start -a android.intent.action.SENDTO -d sms:{number} --es sms_body "{message}"')

# Function to scrape Google search results
def scrape_google():
    query = input("Enter the search query: ")
    url = f'https://www.google.com/search?q={query}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    for item in soup.find_all('h3', limit=5):
        results.append(item.get_text())
    
    print("Top 5 Google search results:")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result}")

# Function to get the current geo coordinates and location
def get_location():
    g = geocoder.ip('me')
    return g.latlng, g.address

# Function to convert text to audio
def text_to_audio():
    text = input("Enter the text to convert to audio: ")
    tts = gTTS(text)
    filename = 'output.mp3'
    tts.save(filename)
    os.system(f'mpg321 {filename}')
    print(f'Audio saved as {filename} and played successfully!')

# Function to set volume
def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        ISimpleAudioVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(ISimpleAudioVolume)
    volume.SetMasterVolume(level, None)
    print(f'Volume set to {level * 100}%')

# Function to crop face from an image
def crop_face(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if faces != ():
        for (x, y, w, h) in faces:
            face = image[y:y+h, x:x+w]
            cv2.imshow('Face', face)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        print("No face detected.")

# Function to apply filters to an image
def apply_filter(image_path, filter_type):
    image = Image.open(image_path)
    if filter_type == 'BLUR':
        filtered_image = image.filter(ImageFilter.BLUR)
    elif filter_type == 'CONTOUR':
        filtered_image = image.filter(ImageFilter.CONTOUR)
    else:
        filtered_image = image
    filtered_image.show()
    print(f'Applied {filter_type} filter to the image.')

# Function to apply cool filters to an image (example given for sunglasses and stars)
def apply_cool_filters(image_path):
    image = Image.open(image_path)

    # Apply sunglasses filter (you can replace this with your sunglasses image)
    sunglasses = Image.open('sunglasses.png')
    sunglasses = sunglasses.resize((200, 50))  # Resize sunglasses to fit the face
    image.paste(sunglasses, (50, 100), sunglasses)  # Adjust position as needed

    # Add star shapes
    draw = ImageDraw.Draw(image)
    for i in range(5):
        draw.polygon([(300 + i*50, 50), (310 + i*50, 100), (350 + i*50, 100),
                      (320 + i*50, 130), (330 + i*50, 180), (300 + i*50, 150),
                      (270 + i*50, 180), (280 + i*50, 130), (250 + i*50, 100),
                      (290 + i*50, 100)], fill="yellow")

    # Save the edited image
    image.save('output_image.jpg')
    image.show()
    print('Cool filters applied and image saved as output_image.jpg.')

# Main menu function
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Send Email")
        print("2. Send SMS from Mobile")
        print("3. Scrape Top 5 Google Search Results")
        print("4. Find Current Geo Coordinates and Location")
        print("5. Convert Text to Audio")
        print("6. Control Volume of Your Laptop")
        print("7. Crop Face from Image")
        print("8. Apply Filters to Image")
        print("9. Apply Cool Filters to Image")
        print("10. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            send_email()
        elif choice == '2':
            send_sms_from_mobile()
        elif choice == '3':
            scrape_google()
        elif choice == '4':
            coords, location = get_location()
            print(f"Coordinates: {coords}, Location: {location}")
        elif choice == '5':
            text_to_audio()
        elif choice == '6':
            level = float(input("Enter volume level (0.0 to 1.0): "))
            set_volume(level)  # Set volume to the specified level
        elif choice == '7':
            image_path = input("Enter the image path: ")
            crop_face(image_path)
        elif choice == '8':
            image_path = input("Enter the image path: ")
            filter_type = input("Enter filter type (BLUR/CONTOUR): ")
            apply_filter(image_path, filter_type)
        elif choice == '9':
            image_path = input("Enter the image path: ")
            apply_cool_filters(image_path)
        elif choice == '10':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
