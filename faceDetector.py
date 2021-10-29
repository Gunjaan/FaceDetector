import cv2
# to import the image
img = cv2.imread("/Users/gunjan/Documents/pins/conan1.jpeg", 0)
face_cascade=cv2.CascadeClassifier("/Users/gunjan/Documents/abstruse/haarcascade_frontalface_default.xml")
img = cv2.imread("/Users/gunjan/Documents/pins/conan1.jpeg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
print(faces)
for x,y,w,h in faces:
    img = cv2.rectangle (img, (x,y), (x+y, y+h), (0,255,0), 2)
cv2.imshow("Conan Gray", img)
cv2.waitKey(6000)
cv2.destroyAllWindows()