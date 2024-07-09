import cv2
cap = cv2.VideoCapture(0)
status,photo = cap.read()
print(status)
cv2.imshow("Image Window",photo)
cv2.imwrite("Photo.jpg",photo)
cv2.waitKey()
cv2.destroyAllWindows()
