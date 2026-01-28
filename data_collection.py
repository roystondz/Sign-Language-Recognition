import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import time

cap = cv2.VideoCapture(1)
detector = HandDetector(maxHands=1)

offset=20
imageSize = 300

folder = "Data/B"
counter=0

while True:
    ret, image = cap.read()

    if not ret:
        print("❌ Failed to grab frame")
        break

    hands, image = detector.findHands(image)
    
    if hands:
        hand =hands[0]
        x,y,w,h=hand['bbox']
        
        imageWhite = np.ones((imageSize, imageSize, 3), np.uint8)*255
        
        
        # Scale factor
        scale = imageSize / max(h, w)

        newW = int(w * scale)
        newH = int(h * scale)

        imageCrop = image[y-offset:y+h+offset, x-offset:x+w+offset]
        imageResize = cv2.resize(imageCrop, (newW, newH))

        # Center the image
        xOffset = (imageSize - newW) // 2
        yOffset = (imageSize - newH) // 2
        
        imageWhite[yOffset:yOffset+newH, xOffset:xOffset+newW] = imageResize
        
        cv2.imshow("Image Crop", imageCrop)
        cv2.imshow("Image White", imageWhite)
        
        
    cv2.imshow("Image", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        counter += 1
        cv2.imwrite(f'{folder}/image_{int(time.time())}_.jpg', imageWhite)
        print(f"Saved image {counter}")

cap.release()
cv2.destroyAllWindows()