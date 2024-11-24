from ultralytics import YOLO
import cv2

model = YOLO("chief_gear.pt")

image = cv2.imread("image.png")

results = model("image.png")

for box in results[0].boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    cropped = image[y1:y2, x1:x2]
    
    cv2.imwrite(f"cropped_{x1}_{y1}.png", cropped)