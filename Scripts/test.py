from ultralytics import YOLO
import os

folder_path = "../demoVideos"
model = YOLO("../runs/detect/train2/weights/best.pt")

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):  # Check if it's a file
        model.predict(file_path, conf=0.4, save=True)