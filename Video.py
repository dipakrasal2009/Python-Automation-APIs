import cv2

cap1 = cv2.VideoCapture(0)
while True:
    status, photo = cap1.read()
    #photo[20:40] = [0,0,255]
    cv2.imshow("Dipak image",photo)
    if cv2.waitKey(5) ==13:
        break

#print(photo)
cv2.destroyAllWindows()
