import cv2

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

crop_face()
