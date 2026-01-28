import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np

cap = cv2.VideoCapture(1)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
with open("Model/labels.txt", "r") as f:
    labels = [line.strip().split()[-1] for line in f.readlines()]

offset = 20
imageSize = 300

index = -1

while True:
    ret, image = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    imageOutput = image.copy()
    hands, image = detector.findHands(image, draw=False)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        # Clamp values to image boundaries
        x1 = max(0, x - offset)
        y1 = max(0, y - offset)
        x2 = min(image.shape[1], x + w + offset)
        y2 = min(image.shape[0], y + h + offset)

        imageCrop = image[y1:y2, x1:x2]

        if imageCrop.size != 0:
            imageWhite = np.ones((imageSize, imageSize, 3), np.uint8) * 255

            hCrop, wCrop, _ = imageCrop.shape
            scale = imageSize / max(hCrop, wCrop)

            newW = int(wCrop * scale)
            newH = int(hCrop * scale)

            imageResize = cv2.resize(imageCrop, (newW, newH))

            xOffset = (imageSize - newW) // 2
            yOffset = (imageSize - newH) // 2

            imageWhite[yOffset:yOffset+newH, xOffset:xOffset+newW] = imageResize

            prediction, index = classifier.getPrediction(imageWhite, draw=False)
            confidence = prediction[index] if index != -1 else 0
            if confidence < 0.2:
                index = -1
            
 

    # Safe label display
    if index != -1:
        cv2.putText(
            imageOutput,
            f"Prediction: {labels[index]}",
            (40, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            4,
            (255, 0, 0),
            10
        )

    cv2.imshow("Image", imageOutput)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()